class Point:
   def __init__(self, x, y):
       self.x = x
       self.y = y
   def move(self):
      print("Move")
   
   def draw(self):
      print("Draw")
      
point1 = Point(50, 60)
point2 = Point(10, 20)
print(point1.x)
print(point2.y)

class Person:
   def __init__(self, name):
      self.name = name
   
   
   def talk(self):
      print(f"Hello there! I am {self.name}")
      print("I am talking.")

person1 = Person("Hemant")
person1.talk()

person2 = Person("Ram")
person2.talk()