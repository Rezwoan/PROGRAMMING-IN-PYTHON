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
def prompt_integer(prompt: str, min_value: int | None = None, max_value: int | None = None) -> int:
    while True:
        raw = input(prompt).strip()
        try:
            val = int(raw)
        except ValueError:
            print("--- Please enter a valid integer. ---")
            continue
        if min_value is not None and val < min_value:
            print(f"--- Value must be >= {min_value}. ---")
            continue
        if max_value is not None and val > max_value:
            print(f"--- Value must be <= {max_value}. ---")
            continue
        return val
#App actions implementation
#Function to add student
def add_student(students: list[dict]) -> None:
    #Calculate student info frm user and compute results
    sid = prompt_non_empty("Enter student ID: ")
    name = clean_name(prompt_non_empty("Enter student name: "))
    n = int(prompt_non_empty("Enter number of subjects: "))
    
    
    
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