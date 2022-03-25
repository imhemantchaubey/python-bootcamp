coordinates = (1, 2, 3)
one = coordinates[0] * coordinates[1] * coordinates[2]
print(one)

x = coordinates[0]
y = coordinates[1]
z = coordinates[2]
two = x * y * z
print(two)

# Now, the same thing can be achieved in the following manner which is called unpacking in python
m, n, o = coordinates
print(m)
print(n)
print(o)
print(m*n*o)

#This can also be used with python lists.