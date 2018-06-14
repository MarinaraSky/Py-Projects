#!/usr/bin/env python3


def common(aList, bList):
    same = list()
    for x in aList:
        for y in bList:
            if x is y:
                same.append(x)
    return same


def main():
    aList = [0, "bird", 1.2, 50]
    bList = [1, 50, "bird", 12]
    print(common(aList, bList))


if __name__ == "__main__":
    main()
