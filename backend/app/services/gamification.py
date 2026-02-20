from sqlalchemy.orm import Session

from ..models import Achievement, User


BADGES = [
    (100, "Bronze Scholar", "Scored 100 points"),
    (250, "Silver Scholar", "Scored 250 points"),
    (500, "Gold Scholar", "Scored 500 points"),
]


def add_points(db: Session, user: User, score: float) -> None:
    gained = max(5, int(score // 10) * 5)
    user.points += gained
    user.level = max(1, user.points // 100 + 1)

    for threshold, badge, description in BADGES:
        exists = (
            db.query(Achievement)
            .filter(Achievement.user_id == user.id, Achievement.badge == badge)
            .first()
        )
        if user.points >= threshold and not exists:
            db.add(Achievement(user_id=user.id, badge=badge, description=description))
