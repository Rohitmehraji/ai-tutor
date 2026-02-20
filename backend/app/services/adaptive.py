
def recommend_next_step(score: float, current_difficulty: str) -> tuple[str, str, str]:
    order = ["easy", "medium", "hard"]
    idx = order.index(current_difficulty)

    if score >= 85 and idx < 2:
        next_diff = order[idx + 1]
        tip = "Great work. Moving you to a more challenging pathway."
    elif score < 50 and idx > 0:
        next_diff = order[idx - 1]
        tip = "Let's reinforce fundamentals before progressing."
    else:
        next_diff = current_difficulty
        tip = "Continue on the same pathway with targeted practice."

    topic = {
        "easy": "core concepts revision",
        "medium": "guided problem solving",
        "hard": "advanced application tasks",
    }[next_diff]
    return next_diff, tip, topic
