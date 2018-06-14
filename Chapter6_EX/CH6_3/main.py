#!/usr/bin/env python3

import sys


def main():
    args = sys.argv
    args.remove(sys.argv[0])
    print(sorted(args))


if __name__ == "__main__":
    main()
