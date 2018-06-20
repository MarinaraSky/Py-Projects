#!/usr/bin/env python3

class Person:

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

class Family:

    def __init__(self, *family):
        self.family = list(family)

    def __str__(self):
        p = ""
        for x in range(0, len(self.family)):
            p += self.family[x].name + " : " +\
            str(self.family[x].age) + " : " +\
            self.family[x].gender + "\n"
        return p

    def add(self, addition):
        self.family.append(addition)


def main():
    p1 = Person("Micheal", 45, "M")
    p2 = Person("Mary", 34, "F")
    p3 = Person("John", 4, "M")
    p4 = Person("A", 5, "F")
    kid = (p3, p4)
    f1 = Family(p1, p2, p3, p4)
    p5 = Person("B", 3, "M")
    f1.add(p5)
    print(f1)
if __name__ == "__main__":
    main()
