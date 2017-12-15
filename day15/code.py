#!/usr/bin/env python3
# -*- coding: utf-8 -*-

PUZZLE_INPUT = [516, 190]


def part1(puzzle_input):
    genA = puzzle_input[0]
    genB = puzzle_input[1]
    matches = 0
    for _ in range(40000000):
        genA = (genA * 16807) % 2147483647
        genB = (genB * 48271) % 2147483647
        if ((genA & 65535) == (genB & 65535)):
            matches += 1
    return matches


def part2(puzzle_input):
    genA = puzzle_input[0]
    genB = puzzle_input[1]
    genA_values = []
    genB_values = []
    while len(genA_values) < 5000000:
        genA = (genA * 16807) % 2147483647
        if (genA % 4 == 0):
            genA_values.append(genA)
    while len(genB_values) < 5000000:
        genB = (genB * 48271) % 2147483647
        if (genB % 8 == 0):
            genB_values.append(genB)
    matches = 0
    for i in range(5000000):
        if ((genA_values[i] & 65535) == (genB_values[i] & 65535)):
            matches += 1
    return matches


print(part1(PUZZLE_INPUT))
print(part2(PUZZLE_INPUT))
