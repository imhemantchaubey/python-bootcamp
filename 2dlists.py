matrix = [
   [1, 2, 3],
   [4, 5, 6],
   [7, 8, 9]
]

print(matrix[0])
print(matrix[0][1])

matrix[2][1] = 20
print(matrix)

for row in matrix:
   for item in row:
      print(item)
      
for row in matrix:
   print(row)