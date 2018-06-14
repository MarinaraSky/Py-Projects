#!/usr/bin/env python3


def onlyPos(*posList, num=0):
    count = 0
    for x in posList:
        if x > num:
            count += 1
    return count


def main():
    print(onlyPos(5, -10, 10, -20, 30, num=0))


if __name__ == "__main__":
    main()
