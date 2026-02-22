"""This module contains functions for grading students based on their marks."""

from __future__ import annotations

# Function to compute total and percentage from marks list
def compute_total_and_percentage(marks: list[float]) -> tuple[float, float]:
    total = 0.0
    for m in marks:
        total += m
    percentage = total / len(marks)*100.0
    return total, percentage

# Function to compute grade from percentage
def grade_from_percentage(percentage: float) -> str:
    if percentage >= 90.0:
        return "A"
    elif percentage >= 85.0:
        return "A+"
    elif percentage >= 80.0:
        return "B+"
    elif percentage >= 75.0:
        return "B"
    elif percentage >= 70.0:
        return "C+"
    elif percentage >= 65.0:
        return "C"
    elif percentage >= 60.0:
        return "D+"
    elif percentage >= 50.0:
        return "D"
    else:
        return "F"

# Function to compute pass/fail status
def status_from_percentage(percentage: float) -> str:
    return "Pass" if percentage >= 50.0 else "Fail"