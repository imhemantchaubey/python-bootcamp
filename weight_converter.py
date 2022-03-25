weight = input("Weight: ")
unit = input("Lbs or kg: ")
if unit.upper() == "LBS":
   converted = float(weight) * 0.45
   print(f"Your are {converted} kilograms...")
else:
   converted = float(weight) / 0.45
   print(f"Your are {converted} pounds...")