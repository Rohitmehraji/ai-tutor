from collections import Counter

from sqlalchemy.orm import Session

from ..models import Progress


def generate_recommendations(db: Session, user_id: int) -> tuple[list[str], list[str]]:
    entries = db.query(Progress).filter(Progress.user_id == user_id).all()
    if not entries:
        return ["number sense", "reading comprehension"], ["starter quiz", "flashcards"]

    weak_topics = [p.topic for p in entries if p.score < 70]
    common = Counter(weak_topics or [p.topic for p in entries]).most_common(3)
    topics = [name for name, _ in common]

    exercises = []
    for topic in topics:
        exercises.extend([
            f"{topic} - adaptive quiz",
            f"{topic} - real-world scenario",
        ])
    return topics, exercises[:6]
