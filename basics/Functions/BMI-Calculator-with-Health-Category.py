# BMI Calculator with Health Category.

def bmi(weight, height):

    bmi_value = weight / (height ** 2)
    
    if bmi_value < 18.5:
        category = "Underweight"
    elif bmi_value < 25:
        category = "Normal weight"
    elif bmi_value < 30:
        category = "Overweight"
    else:
        category = "Obesity"
    
    return bmi_value, category

w = float(input("Enter your weight in kilograms: "))
h = float(input("Enter your height in meters: "))

bmi_result, health_category = bmi(w, h)

print(f"Your BMI is: {bmi_result:.2f}")
print(f"Health category: {health_category}")