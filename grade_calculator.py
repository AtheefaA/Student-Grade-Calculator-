def calculate_grade(marks):
    if marks >= 90:
        return "A", "Excellent! Keep shining! 🌟"
    elif marks >= 80:
        return "B", "Very Good! Keep it up! 👍"
    elif marks >= 70:
        return "C", "Good Job! Keep improving! 😊"
    elif marks >= 60:
        return "D", "You passed! Work a little harder! 💪"
    else:
        return "F", "Don't give up! Practice and try again! ❤️"

student_name = input("Enter student name: ")

while True:
    try:
        marks = int(input("Enter marks (0-100): "))

        if 0 <= marks <= 100:
            break
        else:
            print("Please enter marks between 0 and 100.")
    except ValueError:
        print("Invalid input. Please enter a number.")

grade, message = calculate_grade(marks)

print("\n📊 RESULT")
print("----------------------")
print("Student Name:", student_name)
print("Marks:", marks)
print("Grade:", grade)
print("Message:", message)