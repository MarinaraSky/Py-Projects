#!/usr/bin/env python3

class Person:
    name = ""
    age = int()
    gender = ""

    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender

    def __str__(self):
        return self.name + " : " + str(self.age) + " : " + self.gender

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        self._name = name

    @property
    def age(self):
        return self._age

    @age.setter
    def age(self, age):
        self._age = age

    @property
    def gender(self):
        return self._gender

    @gender.setter
    def gender(self, gender):
        self._gender = gender


def main():
    p1 = Person("Micheael", 45, "M")
    print(p1)

if __name__ == "__main__":
    main()
