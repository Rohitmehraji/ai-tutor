from app.services.adaptive import recommend_next_step


def test_promotes_difficulty_for_high_score():
    next_diff, _, _ = recommend_next_step(90, "easy")
    assert next_diff == "medium"


def test_demotes_difficulty_for_low_score():
    next_diff, _, _ = recommend_next_step(30, "hard")
    assert next_diff == "medium"
