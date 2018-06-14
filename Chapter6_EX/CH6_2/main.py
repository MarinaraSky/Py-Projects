#!/usr/bin/env python3

import myMods
import myMods2


def main():
    firstNum = 2
    secNum = 15
    print(myMods.add(firstNum, secNum))
    print(myMods.sub(firstNum, secNum))
    print(myMods.mul(firstNum, secNum))
    print(myMods.div(firstNum, secNum))
    print(myMods2.add(firstNum, secNum))

if __name__ == "__main__":
    main()
