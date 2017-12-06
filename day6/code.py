#!/usr/bin/env python3
# -*- coding: utf-8 -*-


def part1(in_data):
    blocks = [int(x) for x in in_data.split("\t")]
    states = [tuple(blocks)]
    counter = 0
    while True:
        max_block = max(blocks)
        max_index = blocks.index(max_block)
        blocks[max_index] = 0
        current_idx = max_index + 1
        counter += 1
        while max_block > 0:
            if (current_idx == len(blocks)):
                current_idx = 0
            blocks[current_idx] += 1
            max_block -= 1
            current_idx += 1
        if (tuple(blocks) in states):
            return counter
        else:
            states.append(tuple(blocks))


def part2(in_data):
    blocks = [int(x) for x in in_data.split("\t")]
    states = [tuple(blocks)]
    duplicates = []
    dup_counters = {}
    while True:
        max_block = max(blocks)
        max_index = blocks.index(max_block)
        blocks[max_index] = 0
        current_idx = max_index + 1
        while max_block > 0:
            if (current_idx == len(blocks)):
                current_idx = 0
            blocks[current_idx] += 1
            max_block -= 1
            current_idx += 1
        for st in dup_counters.keys():
            dup_counters[st] += 1
        if tuple(blocks) in duplicates:
            return dup_counters[tuple(blocks)]
        elif (tuple(blocks) in states):
            duplicates.append(tuple(blocks))
            dup_counters[tuple(blocks)] = 0
        else:
            states.append(tuple(blocks))


with open("input.txt", "r") as in_file:
    in_data = in_file.read().strip()


print(part1(in_data))
print(part2(in_data))
