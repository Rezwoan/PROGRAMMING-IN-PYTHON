"""This module contains functionalities related to student list manipulation"""

from __future__ import annotations
from utils import prompt_non_empty, clean_name, prompt_integer, prompt_float
from grading import compute_total_and_percentage, grade_from_percentage, status_from_percentage


def print_student_report(student: dict):
    print("\n"+"-"*40)
    print(f"Student: {student['name']} | (ID: {student['id']})")
    print(f"Subjects: {', '.join(student['subjects'])}")
    print(f"Marks: {', '.join(str(m) for m in student['marks'])}")
    print(f"Total: {student['total']:.2f} ")
    print(f"Percentage: {student['percentage']:.2f}%")
    print(f"Grade: {student['grade']} ")
    print(f"Status: {student['status']} ")
    print("-"*40 + "\n")
    
    
def list_students(students: list[dict]) -> None:
    
    if len(students) == 0:
        print("--- No students added yet. ---")
        return
    print("\n===All Student (Summary) ===")
    for idx, student in enumerate(students, start=1):
        print(f"{student['id']} | {student['name']} | {student['percentage']:.2f}% | {student['grade']} | {student['status']}")
        print()
    

#App actions implementation
#Function to add student
def add_student(students: list[dict]) -> None:
    #Calculate student info frm user and compute results
    sid = prompt_non_empty("Enter student ID: ")
    name = clean_name(prompt_non_empty("Enter student name: "))
    n = prompt_integer(prompt_non_empty("Enter number of subjects: "), min_val=1, max_val=10)
    subjects: list[str] = []
    marks: list[float] = []
    
    # We write a for loop to collect subjects + marks
    for i in range(0, n):
        sub = prompt_non_empty(f"Subject {i+1} name: ")
        subject = sub.strip().title()
        subjects.append(subject)
        mark = prompt_float(f"Enter marks for Subject {i+1}: ", min_val=0.0, max_val=100.0)
        marks.append(mark)
    
    # Compute
    total, percentage = compute_total_and_percentage(marks)
    grade = grade_from_percentage(percentage)
    status = status_from_percentage(percentage)
    student = {
        "id": sid,
        "name": name,
        "subjects": subjects,
        "marks": marks,
        "total": total,
        "percentage": percentage,
        "grade": grade,
        "status": status
    }
    students.append(student)
    print_student_report(student)
    
#find student by id
def find_student_by_id(students: list[dict], sid: str) -> dict | None:
    for student in students:
        if student['id'] == sid:
            return student
    return None

def search_student(students: list[dict]) -> None:
    sid = prompt_non_empty("Enter student ID to search: ")
    student = find_student_by_id(students, sid)
    if student is not None:
        print_student_report(student)
    else:
        print(f"--- No student found with ID: {sid} ---")
        

def delete_student_by_id(students: list[dict], sid: str) -> bool:
    student = find_student_by_id(students, sid)
    if student is None:
        return False #control return
    students.remove(student)
    return True

def delete_student(students: list[dict]) -> None:
    sid = prompt_non_empty("Enter student ID to delete: ")
    if delete_student_by_id(students, sid):
        print(f"--- Student with ID: {sid} has been deleted. ---")
    else:
        print(f"--- No student found with ID: {sid} ---")