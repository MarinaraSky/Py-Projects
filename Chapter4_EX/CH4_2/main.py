#!/usr/bin/env python3


def main():
    userSet = set()
    while True:
        userInput = input("enter a line (q to quit)")
        if userInput == "q":
            break
        userInput = userInput.split()
        for x in userInput:
            userSet.add(x)
    print(sorted(userSet))
    print(len(userSet))


if __name__ == "__main__":
    main()
