students = []  # List of dictionaries. Each dictionary will hold a student's name and a list of their grades
_student_names = set()  # A set that stores student names to optimize the search


def validate_input_name(user_input):
    """Validates that the provided name is non-empty and contains only letters.

    This function checks whether the given string is not empty and consists
    solely of alphabetic characters (spaces are allowed but ignored during
    validation). It is typically used to validate user-provided names before
    adding them to the students list.

    Args:
        user_input (str): The input string representing the student's name.

    Returns:
        bool: True if the input is non-empty and contains only letters
            (ignoring spaces); False otherwise.
    """
    return False if (not user_input or not user_input
                     .replace(" ", "")
                     .replace("-", "")
                     .replace("'", "")
                     .isalpha()) else True


def calculate_average(grades):
    """Calculates the average value of a list of grades.

    This function computes the arithmetic mean of the provided list of numeric
    grades and returns the result rounded to one decimal place.

    Args:
        grades (list[int | float]): A list of numeric grade values.
            The list must not be empty.

    Returns:
        float: The average grade rounded to one decimal place.

    Raises:
        ZeroDivisionError: If the `grades` list is empty.
        TypeError: If the list contains non-numeric values.
    """
    return round(sum(grades) / len(grades), 1)


def add_student():
    """Adds a new student to the list of students after validating the input.

    This function prompts the user to enter a student's name, validates it using
    `validate_input_name`, and then checks whether the student already exists in
    the system. If the student is new, the name is added to the `_student_names`
    set and a corresponding record is appended to the `students` list.
    """
    user_input = input("Enter student name: ").strip().title()

    if not validate_input_name(user_input):
        print("Invalid input. Please enter a student name that non-empty and contain only letters.")
        return

    if user_input in _student_names:
        print(f"Student {user_input} already exists.")
    else:
        _student_names.add(user_input)
        students.append({"name": user_input, "grades": []})


def add_grades():
    """Adds grades to an existing student after validating input.

    This function promts the user to enter a student's name, validates it
    using `validate_input_name`, and searches for the student in the global
    `students` list. If the student exists, the function repeatedly promts
    the user to enter grades until 'done' is entered. Each grade is validated
    to ensure it is an integer between 0 and 100 before being added to the
    student's record.
    """
    name = input("Enter student name: ").strip().title()

    if not validate_input_name(name):
        print("Invalid input. Please enter a student name that non-empty and contain only letters.")
        return

    is_student_found = False

    for student in students:
        if student["name"] == name:
            is_student_found = True

            while True:
                user_input = input("Enter a grade (or 'done' to finish): ").strip().lower()

                if user_input == "done":
                    break

                try:
                    grade = int(user_input)

                    if 0 <= grade <= 100:
                        student["grades"].append(grade)
                    else:
                        print("Invalid input. Grade must be between 0 and 100.")
                except ValueError:
                    print("Invalid input. Please enter a number.")

    if not is_student_found:
        print(f"Student {name} doesn't exist.")
        return


def generate_report():
    """Generates and prints a summary report of all students and their average grades.

    This function iterates through the global `students` list and prints each
    student's average grade. If a student has no grades, "N/A" is displayed
    instead. After listing individual result, the function prints additional
    statistics: the highest average grade, the lowest average grade, and the
    overall average across all students who have at least one grade.
    """
    average_grades = []

    print("--- Student Report ---")

    for student in students:
        try:
            grades = student["grades"]
            average_grade = calculate_average(grades)
            average_grades.append(average_grade)
        except ZeroDivisionError:
            average_grade = "N/A"

        print(f"{student['name']}'s average grade is {average_grade}.")

    if students and average_grades:
        max_average_grade = max(average_grades)
        min_average_grade = min(average_grades)
        overall_average_grade = calculate_average(average_grades)

        print("-" * 26)
        print(f"Max Average: {max_average_grade}")
        print(f"Min Average: {min_average_grade}")
        print(f"Overall Average: {overall_average_grade}")
    else:
        print("No students found or no grades were entered.")


def find_top_student():
    """Finds and prints the student with the highest average grade.

    This function searches through the global `students` list and identifies
    the student with the highest average grade. Students with no grades are
    treated as having an average of 0 for comparison purposes. If a top
    student is found, their name and average grade are printed. If no
    students exist or no grades have been entered, a corresponding message
    is displayed.
    """
    if students:
        top_student = max(students,
                          key=lambda student: round(sum(student["grades"]) / len(student["grades"]), 1)
                          if student["grades"] else 0)

        if top_student:
            try:
                top_student_average = calculate_average(top_student["grades"])
                print(
                    f"The student with highest average is {top_student['name']} with a grade of {top_student_average}")
            except ZeroDivisionError:
                print("No grades have been entered.")
    else:
        print("No students found or no grades were entered.")


class MenuChoiceError(Exception):
    """Raised when a menu choice is invalid"""
    pass


def main_menu_loop():
    """Displaying intercative menu and handling user choices.

    The loop continuously displays menu options and processes user input until
    the exit option is selected. Handles invalid choices and unexpected errors
    without terminating program.

    Menu options:
        - Add a new student
        - Add a grades for a student
        - Show all students
        - Find top performer
        - Exit
    """
    actions = {
        "1": add_student,
        "2": add_grades,
        "3": generate_report,
        "4": find_top_student,
        "5": lambda: print("Exiting program.")
    }

    while True:
        print("\n--- Student Grade Analyzer ---")
        print("1. Add a new student")
        print("2. Add grades for a student")
        print("3. Generate a full report")
        print("4. Find the top student")
        print("5. Exit program")

        try:
            choice = input("Enter your choice: ").strip()

            if choice not in actions:
                raise MenuChoiceError("Invalid choice. Please select one of the suggested options (1-5).")
            elif choice == "5":
                actions[choice]()
                break
            else:
                actions[choice]()
        except MenuChoiceError as mce:
            print(mce)
        except (EOFError, KeyboardInterrupt):
            print("\nExiting program.")
            break
        except Exception as e:
            print("Unexpected error:", e)
            break


main_menu_loop()
