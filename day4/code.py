#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import itertools


def part1(in_data):
    valids = 0
    for line in in_data.split("\n"):
        l_list = line.split(" ")
        l_set = set(l_list)
        if (len(l_list) == len(l_set)):
            valids += 1
    return valids


def part2(in_data):
    valids = 0
    p1_valid = []
    for line in in_data.split("\n"):
        l_list = line.split(" ")
        l_set = set(l_list)
        if (len(l_list) == len(l_set)):
            p1_valid.append(l_list)
    for i in p1_valid:
        ok = True
        for word in i:
            anagrams = ["".join(perm) for perm in itertools.permutations(word)]
            present_anagr = [x for x in i if x in anagrams]
            if (len(present_anagr) > 1):
                ok = False
                break
        if ok:
            valids += 1
    return valids


with open("input.txt", "r") as in_file:
    in_data = in_file.read().strip()


print(part1(in_data))
print(part2(in_data))
