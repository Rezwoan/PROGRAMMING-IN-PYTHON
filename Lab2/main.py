"""
This is a CLI application to calculate student results.
And (possibly) export to a .csv file.
"""

#CLI menu printing function
def print_menu() -> None:
    print("=== Student Results Calculator ===")
    print("1) Add Student + compute results")
    print("2) List students list and result summary")
    print("3) Search student by ID")
    print("4) Delete student by ID")
    print("5) Export all results to CSV")
    print("6) Exit")

# Helper functions
# Function to prompt user to provide non-empty value
def prompt_non_empty(prompt: str) -> str:
    while True:
        s = input(prompt).strip()
        if s:            
            return s
        else:
            print("--- Empty input is not allowed. Try again. ---")
            
# Function to input name and clean it
def clean_name(raw_name: str) -> str:
    return raw_name.strip().title()

# Function to input integer
def prompt_integer(prompt: str, min_val: int | None = None, max_val: int | None = None) -> int:
    while True:
        raw = input(prompt).strip()
        try:
            val = int(raw)
        except ValueError:
            print("--- Please enter a valid integer. ---")
            continue
        if min_val is not None and val < min_val:
            print(f"--- Value must be >= {min_val}. ---")
            continue
        if max_val is not None and val > max_val:
            print(f"--- Value must be <= {max_val}. ---")
            continue
        return val
    
def prompt_float(prompt:str, min_val: float | None = None, max_val: float | None = None) -> float:
    while True:
        raw = input(prompt).strip()
        try:
            val = float(raw)
        except ValueError:
            print("--- Please enter a valid float. ---")
            continue
        if min_val is not None and val < min_val:
            print(f"--- Value must be >= {min_val}. ---")
            continue
        if max_val is not None and val > max_val:
            print(f"--- Value must be <= {max_val}. ---")
            continue
        return val
    
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

def main() -> None:
    #List to contain students' information
    students: list[dict] = [] # With annotation
    
    #print_menu()
    while True:
        print_menu()
        choice = input("Choose an option (1-6): ").strip()
        
        #match-case is only available in python 3.10+
        match choice:
            case "1":
                print("Adding student and computing results...")
                add_student(students)
            case "2":
                print("Listing students and result summary...")
            case "3":
                print("Searching student by ID...")
            case "4":
                print("Deleting student by ID...")
            case "5":
                print("Exporting results to CSV...")
            case "6":
                print("Exiting the application.")
                break
            case _:
                print("--- Invalid choice. Please enter a number (1-6).---")
    
if __name__ == "__main__":
    main()