from datetime import datetime
from typing import Any, Literal

from pydantic import BaseModel, EmailStr, Field


class UserCreate(BaseModel):
    email: EmailStr
    full_name: str
    password: str
    preferred_language: str = "en"
    role: Literal["student", "teacher", "parent"] = "student"


class UserOut(BaseModel):
    id: int
    email: EmailStr
    full_name: str
    preferred_language: str
    role: str
    points: int
    level: int

    class Config:
        from_attributes = True


class Token(BaseModel):
    access_token: str
    token_type: str = "bearer"


class LoginRequest(BaseModel):
    email: EmailStr
    password: str


class ProgressCreate(BaseModel):
    topic: str
    score: float = Field(ge=0, le=100)
    difficulty: Literal["easy", "medium", "hard"]
    response_time: float = Field(gt=0)
    is_correct: bool
    details: dict[str, Any] = {}


class ProgressOut(BaseModel):
    id: int
    topic: str
    score: float
    difficulty: str
    response_time: float
    is_correct: bool
    details: dict[str, Any]
    created_at: datetime

    class Config:
        from_attributes = True


class AdaptiveResponse(BaseModel):
    next_difficulty: str
    pathway_tip: str
    recommended_topic: str


class ChatRequest(BaseModel):
    message: str
    target_language: str | None = None


class ChatResponse(BaseModel):
    reply: str
    detected_language: str
    translated_input: str


class RecommendationOut(BaseModel):
    topics: list[str]
    exercises: list[str]


class VoiceRequest(BaseModel):
    text: str
    language: str = "en"


class VoiceResponse(BaseModel):
    transcript: str
    audio_base64: str


class AnalyticsOut(BaseModel):
    avg_score: float
    completion_rate: float
    difficulty_distribution: dict[str, int]
    recent_activity: list[ProgressOut]
