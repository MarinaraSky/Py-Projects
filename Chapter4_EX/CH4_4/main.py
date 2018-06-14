#!/usr/bin/env python3


def main():
    userDict = {}
    while True:
        try:
            userInput = input("enter a line (q to quit)")
        except EOFError:
            userInput = "q"
        if userInput == "q":
            break
        userInput = userInput.split()
        for x in userInput:
            if userDict.get(x) is None:
                userDict[x] = 1
                print("New")
            else:
                userDict[x] += 1
                print("Updated")
    alphaKeys = sorted(list(userDict.keys()))
    numKeys = list(userDict.keys())
    numKeys.sort(key=userDict.get, reverse=True)
    print(type(numKeys))
    print("Alphabetically Sorted")
    for x in alphaKeys:
        print(x, userDict[x])
    print("Words used most frequently")
    for x in numKeys:
        print(x, userDict[x])


if __name__ == "__main__":
    main()
