from backend.core.retriever import retrieve

query = "AI will replace jobs"
docs = retrieve(query, k=40)

print(f"Retrieved {len(docs)} unique docs")
for i, doc in enumerate(docs):
    print(f"{i+1}. [{doc['label']}] {doc['text']} (score: {doc['score']:.3f})")