from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from .. import schemas
from ..auth import get_current_user
from ..database import get_db
from ..models import Progress, User
from ..services.adaptive import recommend_next_step
from ..services.gamification import add_points
from ..services.recommendation import generate_recommendations

router = APIRouter(prefix="/learning", tags=["learning"])


@router.post("/progress", response_model=schemas.AdaptiveResponse)
def submit_progress(
    payload: schemas.ProgressCreate,
    db: Session = Depends(get_db),
    user: User = Depends(get_current_user),
):
    progress = Progress(user_id=user.id, **payload.model_dump())
    db.add(progress)
    add_points(db, user, payload.score)
    db.commit()

    next_difficulty, pathway_tip, recommended_topic = recommend_next_step(payload.score, payload.difficulty)
    return schemas.AdaptiveResponse(
        next_difficulty=next_difficulty,
        pathway_tip=pathway_tip,
        recommended_topic=recommended_topic,
    )


@router.get("/recommendations", response_model=schemas.RecommendationOut)
def get_recommendations(db: Session = Depends(get_db), user: User = Depends(get_current_user)):
    topics, exercises = generate_recommendations(db, user.id)
    return schemas.RecommendationOut(topics=topics, exercises=exercises)
