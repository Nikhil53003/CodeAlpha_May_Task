def add_grade(grades, subject, grade):
    if subject in grades:
        grades[subject].append(grade)
    else:
        grades[subject] = [grade]

def edit_grade(grades, subject, index, new_grade):
    if subject in grades and 0 <= index < len(grades[subject]):
        grades[subject][index] = new_grade
    else:
        print("Invalid subject or index.")

def delete_grade(grades, subject, index):
    if subject in grades and 0 <= index < len(grades[subject]):
        grades[subject].pop(index)
    else:
        print("Invalid subject or index.")

def calculate_average(grades, subject):
    if subject in grades and grades[subject]:
        return sum(grades[subject]) / len(grades[subject])
    else:
        return 0

def display_grades(grades):
    for subject, grade_list in grades.items():
        print(f"{subject}: {grade_list}")

def display_averages(grades):
    for subject in grades:
        average = calculate_average(grades, subject)
        print(f"Average grade for {subject}: {average:.2f}")

def calculate_total_percentage(grades):
    total_sum = 0
    total_count = 0
    for grade_list in grades.values():
        total_sum += sum(grade_list)
        total_count += len(grade_list)
    if total_count > 0:
        return (total_sum / total_count)
    else:
        return 0

def main():
    grades = {}
    while True:
        print("\nMenu:")
        print("1. Add Grade")
        print("2. Edit Grade")
        print("3. Delete Grade")
        print("4. Calculate Average")
        print("5. Display Grades")
        print("6. Display All Averages")
        print("7. Display Total Percentage")
        print("8. Exit")
        
        choice = input("Enter your choice: ")
        
        if choice == '1':
            subject = input("Enter subject: ")
            try:
                grade = float(input("Enter grade: "))
                add_grade(grades, subject, grade)
            except ValueError:
                print("Invalid input. Please enter a numeric grade.")
        elif choice == '2':
            subject = input("Enter subject: ")
            try:
                index = int(input("Enter index of grade to edit: "))
                new_grade = float(input("Enter new grade: "))
                edit_grade(grades, subject, index, new_grade)
            except ValueError:
                print("Invalid input. Please enter valid numbers.")
        elif choice == '3':
            subject = input("Enter subject: ")
            try:
                index = int(input("Enter index of grade to delete: "))
                delete_grade(grades, subject, index)
            except ValueError:
                print("Invalid input. Please enter valid numbers.")
        elif choice == '4':
            subject = input("Enter subject to calculate average: ")
            average = calculate_average(grades, subject)
            print(f"Average grade for {subject}: {average:.2f}")
        elif choice == '5':
            display_grades(grades)
        elif choice == '6':
            display_averages(grades)
        elif choice == '7':
            total_percentage = calculate_total_percentage(grades)
            print(f"Total percentage of all subjects: {total_percentage:.2f}")
        elif choice == '8':
            break
        else:
            print("Invalid choice, please try again.")

if __name__ == "__main__":
    main()