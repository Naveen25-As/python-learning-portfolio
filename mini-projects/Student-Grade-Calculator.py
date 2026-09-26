# Student Grade Calculator.

def calculate_grade(marks):
    percentage = sum(marks) / len(marks)

    if percentage >= 90:
        grade = "A+"
    elif percentage >= 80:
        grade = "A"
    elif percentage >= 70:
        grade = "B"
    elif percentage >= 60:
        grade = "C"
    elif percentage >= 50:
        grade = "D"
    else:
        grade = "F"

    return percentage, grade


marks = []

print("Enter marks for 5 subjects:")

for i in range(5):
    mark = float(input(f"Subject {i + 1}: "))
    marks.append(mark)

percentage, grade = calculate_grade(marks)

print("\n----- Result -----")
print(f"Total Marks: {sum(marks)}")
print(f"Percentage: {percentage:.2f}%")
print(f"Grade: {grade}")