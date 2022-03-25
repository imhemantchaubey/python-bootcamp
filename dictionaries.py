customer = {
   "name": "Hemant",
   "age": 19,
   "is_verified": True
}
# any key cannot be duplicated similar like dictionaries

print(customer["name"])

# print(customer["Name"])
# print(customer["email"])
# This particular statement shows the error as we are accessing the key which is doesn't exist

print(customer.get("name"))
print(customer.get("email"))        #returns None
print(customer.get("email", "hemant@gmail.com"))

customer["name"] = "Ram"
print(customer["name"])

customer["birthdate"] = "16 Oct 2002"
print(customer["birthdate"])
print(customer)


# Practice
print(list)
digits_mapping = {
   "1": "One",
   "2": "Two",
   '3': 'Three',
   '4': 'Four',
   '5': 'Five',
   '6': 'Six',
   '7': 'Seven',
   "8": "Eight",
   "9": "Nine",
   "0": 'Zero'
}
output = ""
phone = input("Phone: ")
for i in phone:
   output = output + digits_mapping.get(i) + " "
print(output)