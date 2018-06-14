#!/usr/bin/env python3


def getInt():
    while True:
        integer = input("Please enter an Integer(end to quit): ")
        if(integer.replace("-", "").isnumeric()):
            # integer = int(integer)
            return integer
            break
        elif(integer == "end"):
            return integer
            break
        print("You did not enter an integer")


def main():
    mapDict = {"0": "zero", "1": "one", "2": "two",
               "3": "three", "4": "four", "5": "five",
               "6": "six", "7": "seven", "8": "eight",
               "9": "nine"}
    userInt = list(getInt())
    for x in userInt:
        print(mapDict[x])


if __name__ == "__main__":
    main()
