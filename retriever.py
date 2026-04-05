
import faiss
import numpy as np
from app.core.embeddings import get_embedding
import pandas as pd

df = pd.read_csv("app/data/dataset.csv")
texts = df["text"].tolist()

embeddings = get_embedding(texts)
dimension = embeddings.shape[1]

index = faiss.IndexFlatL2(dimension)
index.add(np.array(embeddings))

def retrieve(query, k=5):
    q_emb = get_embedding([query])
    distances, indices = index.search(np.array(q_emb), k)
    return [texts[i] for i in indices[0]]