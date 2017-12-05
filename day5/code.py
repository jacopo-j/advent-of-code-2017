#!/usr/bin/env python3
# -*- coding: utf-8 -*-


def part1(in_data):
    jumps = [int(x) for x in in_data.split("\n")]
    idx = 0
    counter = 0
    while True:
        next_jump = jumps[idx]
        jumps[idx] += 1
        idx += next_jump
        counter += 1
        if (idx < 0) or (idx >= len(jumps)):
            return counter


def part2(in_data):
    jumps = [int(x) for x in in_data.split("\n")]
    idx = 0
    counter = 0
    while True:
        next_jump = jumps[idx]
        if (jumps[idx] >= 3):
            jumps[idx] -= 1
        else:
            jumps[idx] += 1
        idx += next_jump
        counter += 1
        if (idx < 0) or (idx >= len(jumps)):
            return counter


with open("input.txt", "r") as in_file:
    in_data = in_file.read().strip()


print(part1(in_data))
print(part2(in_data))
