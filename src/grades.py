def get_letter_grade(score):
    """Convert a number score to a letter grade"""
    if score is None:
        raise ValueError("Score cannot be None")
    if not isinstance(score, (int, float)):
        raise TypeError("Score must be a number")
    if score < 0 or score > 100:
        raise ValueError("Score must be between 0 and 100")
    if score >= 90:
        return "A"
    elif score >= 80:
        return "B"
    elif score >= 70:
        return "C"
    elif score >= 60:
        return "D"
    else:
        return "F"

def calculate_average(scores):
    """Calculate average of a list of scores"""
    if not scores:
        raise ValueError("Scores list cannot be empty")
    return sum(scores) / len(scores)