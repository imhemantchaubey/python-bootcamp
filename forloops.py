for item in "Hemant":
   print(item)

for item in ["Hemant", "Computer", "Code", "Programming"]:
   print(item)
   
for item in [1, 2, 3, 4, 5]:
   print(item)

for item in range(10):
   print(item)
   
for item in range(5, 10):
   print(item)
   
for item in range(5, 51, 5):
   print(item)

prices = [100, 200, 300]
x = 0
for item in prices:
   x += item
print("The total price:", x)

for x in range(5):
   for y in range(3):
      print(f"({x}, {y})")

numbers = [2, 1, 7, 4, 9, 0, 8]
for i in numbers:
   print('x'*i)
   
numbers = [2, 1, 7, 4, 9, 0, 8]
for x_count in numbers:
   output = ''
   for count in range(x_count):
      output += 'x'
   print(output)

numbers = [1, 1, 1, 1, 1, 1, 6]
for i in numbers:
   print('x '*i)