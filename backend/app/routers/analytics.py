from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from .. import schemas
from ..auth import get_current_user
from ..database import get_db
from ..models import Progress, User

router = APIRouter(prefix="/analytics", tags=["analytics"])


@router.get("/overview/{student_id}", response_model=schemas.AnalyticsOut)
def analytics_overview(
    student_id: int,
    db: Session = Depends(get_db),
    requester: User = Depends(get_current_user),
):
    if requester.role not in {"teacher", "parent"} and requester.id != student_id:
        raise HTTPException(status_code=403, detail="Access denied")

    records = db.query(Progress).filter(Progress.user_id == student_id).order_by(Progress.created_at.desc()).all()
    if not records:
        return schemas.AnalyticsOut(
            avg_score=0,
            completion_rate=0,
            difficulty_distribution={"easy": 0, "medium": 0, "hard": 0},
            recent_activity=[],
        )

    avg_score = sum(r.score for r in records) / len(records)
    completion_rate = (sum(1 for r in records if r.is_correct) / len(records)) * 100
    dist = {"easy": 0, "medium": 0, "hard": 0}
    for rec in records:
        dist[rec.difficulty] += 1

    return schemas.AnalyticsOut(
        avg_score=round(avg_score, 2),
        completion_rate=round(completion_rate, 2),
        difficulty_distribution=dist,
        recent_activity=records[:10],
    )
