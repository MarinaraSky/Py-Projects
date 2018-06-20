#!/usr/bin/env python3

class Worker:

    def __init__(self, name, salary, years):
        self.name = name
        self.salary = salary
        self.years = years

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        self._name = name

    @property
    def salary(self):
        return self._salary

    @salary.setter
    def salary(self, salary):
        self._salary = salary

    @property
    def years(self):
        return self._years

    @years.setter
    def years(self, years):
        self._years = years

    def pention(self):
        return self.years * (self.salary * .1)

class Manager(Worker):

        def pention(self):
            return self.years * (self.salary * .2)

class Executive(Manager):

        def pention(self):
            return self.years * (self.salary * .3)

def main():

    p1 = Worker("Marc", 100000, 3)
    p2 = Manager("Ted", 200000, 5)
    p3 = Executive("Bill", 300000, 10)
    print(p1.pention())

if __name__ == "__main__":
    main()
