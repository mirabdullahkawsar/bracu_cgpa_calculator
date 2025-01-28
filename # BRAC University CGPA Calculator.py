# BRAC University CGPA Calculator

def grade_to_point(grade):
    """Convert letter grade to grade points."""
    grade_scale = {
        'A': 4.0, 'A-': 3.7, 'B+': 3.3, 'B': 3.0, 'B-': 2.7,
        'C+': 2.3, 'C': 2.0, 'C-': 1.7, 'D+': 1.3, 'D': 1.0, 'F': 0.0
    }
    return grade_scale.get(grade.upper(), -1)


def calculate_gpa(grades, credits):
    """Calculate GPA for a semester."""
    total_points = sum(grade_to_point(grade) * credit for grade, credit in zip(grades, credits))
    total_credits = sum(credits)
    return round(total_points / total_credits, 2) if total_credits > 0 else 0.0


def calculate_cgpa(previous_credits, previous_points, current_gpa, current_credits):
    """Calculate CGPA with previous and current semester details."""
    total_credits = previous_credits + current_credits
    total_points = previous_points + (current_gpa * current_credits)
    return round(total_points / total_credits, 2) if total_credits > 0 else 0.0


def main():
    print("Welcome to BRAC University CGPA Calculator!")
    print("1. Calculate Semester GPA")
    print("2. Calculate Cumulative CGPA")
    print("3. Predict Target GPA")
    choice = input("Enter your choice (1/2/3): ")

    if choice == '1':
        num_courses = int(input("Enter the number of courses: "))
        grades = []
        credits = []
        for i in range(num_courses):
            grade = input(f"Enter grade for course {i + 1}: ")
            credit = float(input(f"Enter credit hours for course {i + 1}: "))
            grades.append(grade)
            credits.append(credit)
        semester_gpa = calculate_gpa(grades, credits)
        print(f"Your Semester GPA is: {semester_gpa}")

    elif choice == '2':
        previous_credits = float(input("Enter total completed credits: "))
        previous_points = float(input("Enter total grade points: "))
        current_gpa = float(input("Enter your current semester GPA: "))
        current_credits = float(input("Enter current semester credits: "))
        cgpa = calculate_cgpa(previous_credits, previous_points, current_gpa, current_credits)
        print(f"Your Updated CGPA is: {cgpa}")

    elif choice == '3':
        desired_cgpa = float(input("Enter your target CGPA: "))
        previous_credits = float(input("Enter total completed credits: "))
        previous_points = float(input("Enter total grade points: "))
        remaining_credits = float(input("Enter remaining credits to graduate: "))
        required_gpa = ((desired_cgpa * (previous_credits + remaining_credits)) - previous_points) / remaining_credits
        print(f"To achieve a CGPA of {desired_cgpa}, you need a GPA of: {round(required_gpa, 2)} in remaining credits.")

    else:
        print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
