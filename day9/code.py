#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import re


def part1(in_data):
    data = re.sub(r"!.", "", in_data)
    data = re.sub(r"<[^>]*>", "", data)
    score = 0
    next_score = 1
    for char in data:
        if (char == "{"):
            score += next_score
            next_score += 1
        elif (char == "}"):
            next_score -= 1
    return score


def part2(in_data):
    data = re.sub(r"!.", "", in_data)
    garbage = re.findall(r"<([^>]*)>", data)
    count = 0
    for i in garbage:
        count += len(i)
    return count


with open("input.txt", "r") as in_file:
    in_data = in_file.read().strip()


print(part1(in_data))
print(part2(in_data))
