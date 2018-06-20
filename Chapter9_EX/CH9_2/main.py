#!/usr/bin/env python3
from sys import argv
import argparse

parser = argparse.ArgumentParser(description="Print out lines, words, and characters in a file")
parser.add_argument("filename", metavar="FN", type=argparse.FileType("r"), nargs="+", help="Files to accumulate")
parser.add_argument("--total", dest="total", action="store_true", help="Total lines, words, and chars")

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
    args = parser.parse_args()
    if args.total:
        totalLines = 0
        totalWords = 0
        totalChars = 0
        for currStream in args.filename:
            stream.append(currStream.read())
        for x in range(0, len(stream)):
            totalLines += getLines(stream[x])
            totalWords += getWords(stream[x])
            totalChars += getChars(stream[x])
        print("Total Lines: ", totalLines)
        print("Total Words: ", totalWords)
        print("Total Chars: ", totalChars)
    else:
        for currStream in args.filename:
            stream.append(currStream.read())
        for x in range(0, len(stream)):
            print("File: ", argv[x + 1])
            print("Lines: ", getLines(stream[x]))
            print("Words: ", getWords(stream[x]))
            print("Chars: ", getChars(stream[x]))

if __name__ == "__main__":
    main()
