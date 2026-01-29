from typing import List, Dict
def normalize_scores(scores: List[int]) -> List[int]:
    normalized_scores = [max(0, min(score, 100)) for score in scores]
    return normalized_scores
    """
    Return a new list where each score is clamped to the range [0, 100].
    Example:
    [120, -4, 90] -> [100, 0, 90]
    """
    raise NotImplementedError

def letter_grades(scores: List[int]) -> List[str]:
    """
    Convert numeric scores to letter grades using this scale:
    A: 90-100
    B: 80-89
    C: 70-79
    D: 60-69
    F: 0-59
    Notes:
    - First call normalize_scores(scores)
    - Return a list of letters with the same length as scores
    """
    normalized_scores = normalize_scores(scores)
    letter_grades = [
        "A" if score >= 90 else "B" if score >= 80 else "C" if score >= 70 else "D" if score >= 60 else "F"
        for score in normalized_scores
    ]
    return letter_grades
    raise NotImplementedError

    def grade_histogram(grades: List[str]) -> Dict[str, int]:
        """
        Return a dictionary mapping each letter in {"A","B","C","D","F"} to its count.
        Example:
        ["A","A","C"] -> {"A":2,"B":0,"C":1,"D":0,"F":0}
        """
        histogram = {"A": 0, "B": 0, "C": 0, "D": 0, "F": 0}
        for grade in grades:
            histogram[grade] += 1
        return histogram
        raise NotImplementedError