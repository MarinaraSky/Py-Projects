#!/usr/bin/env python3

import sys


def main():
    sys.argv.remove(sys.argv[0])
    for x in range(0, len(sys.argv)):
        sys.argv[x] = int(sys.argv[x])
    print(sum(sys.argv)/len(sys.argv))
    print(sum(sys.argv))


if __name__ == "__main__":
    main()
