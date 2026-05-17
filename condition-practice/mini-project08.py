# Simple Grade Calculator
# Task:
# Create a program that takes the student's marks in 3 subjects (Math, Science, English).
# Calculate:

# Average marks
# Grade according to this system:
# ≥ 90 → A+
# ≥ 80 → A
# ≥ 70 → B
# ≥ 60 → C
# ≥ 50 → D
# < 50 → F


# Print the average and the grade with a nice message (e.g. "Congratulations!" for A+ or "You need to work harder" for F).

student_marks_math = float(input("Enter marks for Math: "))
student_marks_science = float(input("Enter marks for Science: "))
student_marks_english = float(input("Enter marks for English: "))

average_marks = float((student_marks_math + student_marks_science + student_marks_english) / 3)
print(f"Average marks: {average_marks:.2f}")

if average_marks >= 90:
    grade = 'A+'
    message = "Congratulations! You got an A+!"
elif average_marks >= 80:
    grade = 'A'
    message = "Great job! You got an A!"
elif average_marks >= 70:
    grade = 'B'
    message = "Good effort! You got a B!"
elif average_marks >= 60:
    grade = 'C'
    message = "Not bad! You got a C!"
elif average_marks >= 50:
    grade = 'D'
    message = "You passed! You got a D!"
else:
    grade = 'F'
    message = "You need to work harder. You got an F."

print(f"Average marks: {average_marks:.2f}")
print(f"Grade: {grade}")
print(message)