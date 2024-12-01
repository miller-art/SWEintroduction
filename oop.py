# -*- coding: utf-8 -*-
"""OOPinpython.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1ZILOh2-IcKRuS-eKkEfqiH5G48GWGHSl
"""

class Animal:
    def __init__(self, name):
        self.name = name

    def eat(self):
        print(f"{self.name} is eating.")

    def sleep(self):
        print(f"{self.name} is sleeping.")


class Dog(Animal):
    def bark(self):
        print(f"{self.name} is barking.")


class Cat(Animal):
    def meow(self):
        print(f"{self.name} is meowing.")

dog = Dog("dog")
cat = Cat("cat")

dog.eat()
dog.sleep()
dog.bark()

cat.eat()
cat.sleep()
cat.meow()