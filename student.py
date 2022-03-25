def calculate_total(maths, science, history, english, marathi):
    total_marks = maths + science + history + english + marathi
    return total_marks

def calculate_percentage(total):
    percentage = (total*100)/500
    return percentage

maths = int(input("Enter the marks for maths: "))
science = int(input("Enter the marks for science: "))
history = int(input("Enter the marks for history: "))
english = int(input("Enter the marks for english: "))
marathi = int(input("Enter the marks for marathi: "))

total = calculate_total(maths, science, history, english, marathi)
print(f"Total marks: {total} / 500")
percentage = calculate_percentage(total)
print(f"Percentage: {percentage}")

if percentage>=35:
    print("The student passed...")
else:
    print("The student failed...")