import random

def analyze_answer(answer):
    answer_lower = answer.lower()

    score = 0

    # keyword-based scoring
    if "ai" in answer_lower:
        score += 2
    if "machine learning" in answer_lower or "subset" in answer_lower:
        score += 3
    if "intelligence" in answer_lower or "data" in answer_lower:
        score += 2

    # length-based scoring
    length = len(answer.split())
    if length > 8:
        score += 2
    elif length > 4:
        score += 1

    # penalty cases
    if "don't know" in answer_lower:
        score = 2

    if "ignore" in answer_lower:
        score = 1  # injection handling

    # normalize score to 1–10
    score = max(1, min(10, score))
    return score


# ✅ ADD HERE (outside evaluate)
def explain(score):
    if score <= 3:
        return "Incorrect answer"
    elif score <= 6:
        return "Partially correct"
    else:
        return "Good answer"


def evaluate(prompt_type, answer, runs=3):
    results = []

    for _ in range(runs):
        base = analyze_answer(answer)

        # simulate prompt behavior
        if prompt_type == "basic":
            variation = random.randint(-3, 3)

        elif prompt_type == "structured":
            variation = random.randint(-2, 2)

        elif prompt_type == "strict":
            variation = random.choice([0, 0, 1, -1])  # very stable

        score = base + variation

        # clamp to valid range
        score = max(1, min(10, score))

        reason = explain(score)

        # store score + reason
        results.append((score, reason))

    return results