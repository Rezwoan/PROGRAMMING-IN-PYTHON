"""
This is a CLI application to calculate student results.
And (possibly) export to a .csv file.
"""
from data_processor import compute_total_and_percentage, grade_from_percentage, status_from_percentage, add_student, list_students
from utils import prompt_non_empty, clean_name, prompt_integer, prompt_float


#CLI menu printing function
def print_menu() -> None:
    print("=== Student Results Calculator ===")
    print("1) Add Student + compute results")
    print("2) List students list and result summary")
    print("3) Search student by ID")
    print("4) Delete student by ID")
    print("5) Export all results to CSV")
    print("6) Exit")


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
                list_students(students)
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