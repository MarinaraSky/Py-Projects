#!/usr/bin/env python3


def onlyPos(posList):
    retList = list()
    for x in posList:
        if x > 0:
            retList.append(x)
    return retList


def main():
    numLine = list()
    for x in range(-50, 2):
        numLine.append(x)
    posList = onlyPos(numLine)
    print(posList)


if __name__ == "__main__":
    main()
