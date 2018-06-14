#!/usr/bin/env python3


def main():
    for x in range(0, 50):
        if (x % 10 == 0):
            print()
        xString = "%2d   " % (x)
        print(xString, end="")
    print()


if __name__ == "__main__":
    main()
