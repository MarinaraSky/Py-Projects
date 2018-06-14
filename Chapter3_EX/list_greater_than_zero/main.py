#!/usr/bin/env python3


def isInt(testInt):
    integer = testInt
    if(integer.replace("-", "").isnumeric()):
        return True


def main():
    intInput = input("You will be prompted for integers.: ")
    listInput = intInput.split()

    for x in listInput:
        if isInt(x):
            if int(x) > 0:
                print(x, "is greater than 0")
        else:
            print(x, "is not a number")

if __name__ == '__main__':
    main()
