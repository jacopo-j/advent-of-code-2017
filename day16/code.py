#!/usr/bin/env python3
# -*- coding: utf-8 -*-


def part1(in_data, programs=None):
    if not programs:
        programs = [chr(c) for c in range(ord("a"), ord("q"))]
    moves = in_data.split(",")
    for move in moves:
        if (move[0] == "s"):
            sl = programs[-int(move[1:]):]
            programs = sl + programs[:-int(move[1:])]
        elif (move[0] == "x"):
            a = int(move[1:].split("/")[0])
            b = int(move[1:].split("/")[1])
            programs[a], programs[b] = programs[b], programs[a]
        elif (move[0] == "p"):
            a = programs.index(move[1:].split("/")[0])
            b = programs.index(move[1:].split("/")[1])
            programs[a], programs[b] = programs[b], programs[a]
    return programs


def part2(in_data):
    programs = [chr(c) for c in range(ord("a"), ord("q"))]
    steps = ["".join(programs)]
    for _ in range(0, 1000000000):
        programs = part1(in_data, programs)
        if ("".join(programs) in steps):
            break
        steps.append("".join(programs))
    cycle_length = len(steps)
    correct_pos = 1000000000 % cycle_length
    return steps[correct_pos]


with open("input.txt", "r") as in_file:
    in_data = in_file.read().strip()


print("".join(part1(in_data)))
print(part2(in_data))
