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
    print("You will be prompted to enter three integers.")
    start = getInt()
    stop = getInt()
    step = getInt()
    if start < stop and step > 0:
        for x in range(start, stop, step):
            print(x)
    elif stop < start:
        if step > 0:
            step = step * -1
        for x in range(start, stop, step):
            print(x)

if __name__ == '__main__':
    main()
