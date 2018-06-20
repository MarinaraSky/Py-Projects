#!/usr/bin/env python3
from sys import argv

def getWords(stream):
    fileWords = stream.split()
    return len(fileWords)

def getChars(stream):
    fileChars = "".join(stream)
    return len(fileChars)

def getLines(stream):
    count = 0
    fileLines = stream.split("\n")
    for x in fileLines:
        count += 1
    return count


def main():
    stream = []
    for x in argv[1:]:
        with open(x, "r") as currStream:
            stream.append(currStream.read())
    for x in range(0, len(stream)):
        print("File: ", argv[x + 1])
        print("Lines: ", getLines(stream[x]))
        print("Words: ", getWords(stream[x]))
        print("Chars: ", getChars(stream[x]))
if __name__ == "__main__":
    main()
