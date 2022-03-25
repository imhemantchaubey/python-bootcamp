class Mammal:
   def walk(self):
      print("I am walking...")


class Dog(Mammal):
   def bark(self):
      print("I am barking...")


class Cat(Mammal):
   pass


dog1 = Dog()
dog1.walk()
dog1.bark()

cat1 = Cat()
cat1.walk()