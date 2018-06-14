#!/usr/bin/env python3


def incrementDict(aDict, inc):
    for x in aDict:
        aDict[x] += inc
    return aDict


def main():
    numbers = {"1": 1, "2": 2, "3": 3, "4": 4,
               "5": 5}
    inc = 3
    print(sorted(incrementDict(numbers, inc).items()))


if __name__ == "__main__":
    main()
