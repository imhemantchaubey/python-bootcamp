# def greet_user():
#    print("Hi there!")
#    print("Welcome aboard...")

# print("Start")
# greet_user()
# print("Finish")

def greet_user(first_name, last_name):
   print(f"Hi {first_name} {last_name}!")
   print("Welcome aboard...")
   
print("Start")
greet_user("Hemant", "Chaubey")                               # position argument
greet_user(last_name="Chaubey", first_name="Hemant")          # keyword argument
greet_user("Hemant", last_name="Chaubey")                     # keyword argument
print("Finish")


# return
def square(number):
   return number * number

square_nine = square(9)
print(square_nine)

print(square(25))

# by default python function return None