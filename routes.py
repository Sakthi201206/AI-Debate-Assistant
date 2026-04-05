from fastapi import APIRouter
from app.services.debate_service import generate_debate

router = APIRouter()

@router.post("/debate")
def debate(data: dict):
    topic = data["topic"]
    return generate_debate(topic)