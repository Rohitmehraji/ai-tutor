from fastapi import APIRouter, Depends

from .. import schemas
from ..auth import get_current_user
from ..models import User
from ..services.voice import speech_to_text_simulated, text_to_speech_simulated

router = APIRouter(prefix="/voice", tags=["voice"])


@router.post("/interact", response_model=schemas.VoiceResponse)
def voice_interact(payload: schemas.VoiceRequest, user: User = Depends(get_current_user)):
    transcript = speech_to_text_simulated(payload.text)
    audio = text_to_speech_simulated(transcript, payload.language or user.preferred_language)
    return schemas.VoiceResponse(transcript=transcript, audio_base64=audio)
