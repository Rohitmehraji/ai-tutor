from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from .. import schemas
from ..auth import get_current_user
from ..database import get_db
from ..models import ChatMessage, User
from ..services.chatbot import resolve_doubt
from ..services.nlp import detect_language

router = APIRouter(prefix="/chat", tags=["chat"])


@router.post("/doubt", response_model=schemas.ChatResponse)
def doubt_resolution(
    payload: schemas.ChatRequest,
    db: Session = Depends(get_db),
    user: User = Depends(get_current_user),
):
    detected = detect_language(payload.message)
    target = payload.target_language or user.preferred_language
    translated_input, reply = resolve_doubt(payload.message, detected, target)

    db.add(ChatMessage(user_id=user.id, sender="user", content=payload.message, detected_language=detected))
    db.add(ChatMessage(user_id=user.id, sender="assistant", content=reply, detected_language=target))
    db.commit()

    return schemas.ChatResponse(reply=reply, detected_language=detected, translated_input=translated_input)
