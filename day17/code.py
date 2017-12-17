#!/usr/bin/env python3
# -*- coding: utf-8 -*-

PUZZLE_INPUT = 314


def part1(in_data):
    contents = [0]
    pos = 0
    next_value = 1
    for _ in range(2017):
        pos += in_data
        pos = pos % next_value + 1
        contents.insert(pos, next_value)
        next_value += 1
    return contents[pos + 1]


def part2(in_data):
    pos = 0
    next_value = 1
    for _ in range(50000000):
        pos += in_data
        pos = pos % next_value + 1
        if (pos == 1):
            answer = next_value
        next_value += 1
    return answer


print(part1(PUZZLE_INPUT))
print(part2(PUZZLE_INPUT))
