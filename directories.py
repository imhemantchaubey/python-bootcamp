from pathlib import Path

path = Path()
print(path)

path = Path("C:/Users/heman/Desktop/Programming/Python")
print(path.exists())

path = Path("C:/Users/heman/Desktop/Programming/Hemant")
print(path.exists())

path = Path("C:/Users/heman/Desktop/Programming/Python/Hemant")
print(path.mkdir())

path = Path("C:/Users/heman/Desktop/Programming/Python/Hemant")
print(path.rmdir())

path = Path("C:/Users/heman/Desktop/Programming/Python")
for file in path.glob('*.py'):
   print(file)