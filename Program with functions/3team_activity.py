"""
height in cm, weight in kilograms
"""
from datetime import datetime
 
def computebmi(weight, height):
    bmi = (10000 * weight) / (height ** 2)
    return bmi
 
def computewomenbmr(weight, height, age):
    bmr = 447.593 + (9.247 * weight) + (3.098 * height) - (4.33 * age)
    return bmr
 
def computemenbmr(weight, height, age):
    bmr = 88.362 + (13.397 * weight) + (4.799 * height) - (5.677 * age)
    return bmr
 
def convertweightkg(weight):
  return weight * 0.45359237
 
def convertheightm(height):
  # 1 inch = 2.54 c 
  height * 2.54
  return height / 100
  
def compute_age(birth):
    """Compute and return a person's age in years.
 
    Parameter birth: a person's birthdate stored as
        a string in this format: YYYY-MM-DD
    Return: a person's age in years.
    """
    birthday = datetime.strptime(birth, "%Y-%m-%d")
    today = datetime.now()
 
    # Compute the difference between today and the birthday in years.
    years = today.year - birthday.year
 
    # If necessary, subtract one from the difference.
    if birthday.month > today.month or \
        (birthday.month == today.month and birthday.day > today.day):
        years -= 1
 
    return years
 
def main():
    gender = input("Enter your gender: (M/F) ")
    birth = input("Enter your birthdate: (YYYY-MM-DD) ")
    weight = int(input("Enter your weight in pounds: "))
    height = int(input("Enter your height in inches: "))
    height = convertheightm(height)
    weight = convertweightkg(weight)
    
    age = compute_age(birth)
    bmi = (computebmi(weight, height))
 
    if gender.upper() == "M":
        bmr = computemenbmr(weight, height, age)
    elif gender.upper() == "F":
        bmr = computewomenbmr(weight, height, age)
    print(f"\nAge (years): {age} ")
    print(f"Weight (kg):{weight:.2f}  ")
    print(f"Height (m): {height:.1f} ")
    print(f"Body Mass Index: {bmi:.1f} ")
    print(f"Basal metabolic rate (kcal/day): {bmr:.0f} ")
 
pass
 
main()