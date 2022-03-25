birth_year = int(input("Enter your birth year: "))
print(type(birth_year))
age = 2022 - birth_year
print(type(age))
print("Your age:", age)

weight_pounds = input("Enter your weight in pounds: ")
weight_kilograms = float(weight_pounds)*0.453592
print("Your weight in kilograms: ", weight_kilograms)