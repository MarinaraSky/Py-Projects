#!/usr/bin/env python3


def getInt():
    while True:
        integer = input("Please enter an Integer: ")
        if(integer.replace("-","").isnumeric()):
            integer = int(integer)
            return integer
            break
        print("You did not enter an integer")

def getIncSum(start, end):
    total = 0
    count = start
    while count <= end:
        total = total + count
        count += 1
    return total

def main():
    print("You will be prompted to enter two integers.")
    int1 = getInt()
    int2 = getInt()
    if int1 == int2:
        print("You've entered the same number")
    elif int1 < int2:
        incSum = getIncSum(int1, int2)
        print(incSum)
    else:
        incSum = getIncSum(int2, int1)
        print(incSum)

if __name__ == '__main__':
    main()
