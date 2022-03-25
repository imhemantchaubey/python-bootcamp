names = ["Ram", "Hemant", "Shyam", "Krishna"]
print(names)
print(names[-1])
print(names[2])
print(names[1: 3])
print(names)

names[3] = "Prahlad"
print(names)


numbers = [2, 1, 7, 4, 9, 0, 8]
largest = numbers[0]
for x in numbers:
   if largest < x:
      largest = x
print(f"The largest number = {largest}")

mylist = [1.0, 1, 1]
mylist.remove(1)
print(mylist)