#!/usr/bin/env python3

from collections import Counter


# Counting DNA Nucleotides
def solution(string):
    counts = Counter(string)
    return(str(counts['A']) + str(' ') + str(counts['C']) + str(' ') + str(counts['G']) + str(' ') + str(counts['T']))


def readfile(input_file):
    return input_file.readline().strip()


def main():
    with open("Input.txt", "r") as input_file:
        print(solution(readfile(input_file)))


if __name__ == "__main__":
    main()
