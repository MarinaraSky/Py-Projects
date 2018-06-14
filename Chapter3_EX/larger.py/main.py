#!/usr/bin/env python3


def getInt():
    while True:
        integer = input("Please enter an Integer: ")
        if(integer.replace("-", "").isnumeric()):
            integer = int(integer)
            return integer
            break
        print("You did not enter an integer")


def main():
    print("You will be prompted to enter two integers.")
    int1 = getInt()
    int2 = getInt()
    if int1 == int2:
        print("Your integers are equal.")
    elif int1 < int2:
        outputText = "%d is greater than %d" % (int2, int1)
        print(outputText)
    else:
        outputText = "%d is greater than %d" % (int1, int2)
        print(outputText)

if __name__ == '__main__':
    main()
