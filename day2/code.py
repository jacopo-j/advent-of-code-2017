#!/usr/bin/env python3
# -*- coding: utf-8 -*-


def part1(in_data):
    checksum = 0
    for row in in_data.split("\n"):
        digits = [int(x) for x in row.split("\t")]
        checksum += max(digits) - min(digits)
    return checksum


def part2(in_data):
    checksum = 0
    for row in in_data.split("\n"):
        digits = [int(x) for x in row.split("\t")]
        for digit1 in digits:
            for digit2 in digits:
                if (digit1 != digit2) and (digit1 % digit2 == 0):
                    checksum += digit1 / digit2
    return int(checksum)


with open("input.txt", "r") as input_file:
    in_data = input_file.read().strip()

print(part1(in_data))
print(part2(in_data))