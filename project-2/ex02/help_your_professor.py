def average(dct: dict[str, int]) -> float:
    """receive a dict with names and grades, and return the average grade of class"""
    total = sum(dct.values())
    return total / len(dct) if total else 0
