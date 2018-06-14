#!/usr/bin/env python3


def multiWrapper():
    def multi(multiplicand, plyer):
        return multiplicand * plyer
    return multi


def main():
    multiplicand = 15
    plyer = 5
    print(multiWrapper()(multiplicand, plyer))

if __name__ == "__main__":
    main()
