#!/usr/bin/env python3


def multiWrapper(multiplicand, multiplyer):
    def multi():
        return multiplicand * multiplyer
    return multi()


def main():
    print(multiWrapper(15, 5))


if __name__ == "__main__":
    main()
