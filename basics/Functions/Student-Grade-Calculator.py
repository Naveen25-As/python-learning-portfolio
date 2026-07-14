# Student Grade Calculator.

def calculate_grade(marks):
    average = sum(marks) / len(marks)

    if average >= 90:
        grade = "A+"
    elif average >= 80:
        grade = "A"
    elif average >= 70:
        grade = "B"
    elif average >= 60:
        grade = "C"
    else:
        grade = "Fail"

    return average, grade

marks = []

for i in range(5):
    marks.append(int(input(f"Subject {i+1}: ")))

avg, grade = calculate_grade(marks)

print("Average =", avg)
print("Grade =", grade)