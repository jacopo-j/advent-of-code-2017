#!/usr/bin/env python3
# -*- coding: utf-8 -*-


def part1(in_data):
    instr = in_data.split(",")
    pos = [0, 0, 0]
    for i in instr:
        if (i == "n"):
            pos[0] += 1
            pos[1] -= 1
        elif (i == "s"):
            pos[0] -= 1
            pos[1] += 1
        elif (i == "se"):
            pos[0] -= 1
            pos[2] += 1
        elif (i == "ne"):
            pos[1] -= 1
            pos[2] += 1
        elif (i == "sw"):
            pos[1] += 1
            pos[2] -= 1
        elif (i == "nw"):
            pos[0] += 1
            pos[2] -= 1
    return int((abs(pos[0]) + abs(pos[1]) + abs(pos[2])) / 2)


def part2(in_data):
    instr = in_data.split(",")
    pos = [0, 0, 0]
    max_distance = 0
    for i in instr:
        if (i == "n"):
            pos[0] += 1
            pos[1] -= 1
        elif (i == "s"):
            pos[0] -= 1
            pos[1] += 1
        elif (i == "se"):
            pos[0] -= 1
            pos[2] += 1
        elif (i == "ne"):
            pos[1] -= 1
            pos[2] += 1
        elif (i == "sw"):
            pos[1] += 1
            pos[2] -= 1
        elif (i == "nw"):
            pos[0] += 1
            pos[2] -= 1
        distance = int((abs(pos[0]) + abs(pos[1]) + abs(pos[2])) / 2)
        if (distance > max_distance):
            max_distance = distance
    return max_distance


with open("input.txt", "r") as in_file:
    in_data = in_file.read().strip()


print(part1(in_data))
print(part2(in_data))
