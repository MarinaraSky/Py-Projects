#!/usr/bin/env python3


def sort(aList):
    return sorted(aList)


def reverse(aList):
    return aList[::-1]


def main():
    values = [10, 40, 30, 20, 5]
    print(sort(values))
    print(reverse(values))
    print(reverse(sort(values)))
    print(values)


if __name__ == "__main__":
    main()
