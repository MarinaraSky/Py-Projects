#!/usr/bin/env python3


def multiWrapper():
    return lambda multiplicand, plyer: multiplicand * plyer


def main():
    multiplicand = 15
    plyer = 5
    print(multiWrapper()(multiplicand, plyer))

if __name__ == "__main__":
    main()
