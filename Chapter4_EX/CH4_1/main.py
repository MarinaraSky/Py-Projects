#!/usr/bin/env python3


def getInt():
    while True:
        integer = input("Please enter an Integer: ")
        if(integer.replace("-", "").isnumeric()):
            integer = int(integer)
            return integer
            break
        elif(integer == "end"):
            return integer
            break
        print("You did not enter an integer")


def main():
    duplicates = 0
    userSet = set()
    count = 0
    while True:
        select = getInt()
        if select == "end":
            print("Your set is: ", userSet)
            print("Entries not added to set: ", count - len(userSet))
            break
        count += 1
        userSet.add(select)


if __name__ == '__main__':
    main()
