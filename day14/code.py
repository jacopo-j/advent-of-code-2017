#!/usr/bin/env python3
# -*- coding: utf-8 -*-

PUZZLE_INPUT = "wenycdww"


def knot_hash(in_data):
    # From Day 10
    nlist = list(range(0, 256))
    lengths = [ord(x) for x in list(in_data)] + [17, 31, 73, 47, 23]
    pos = 0
    skip_size = 0
    for _ in range(0, 64):
        for length in lengths:
            sl_end = pos + length
            if (sl_end >= len(nlist)):
                sl_end = pos + length - len(nlist)
                slice_rev = nlist[pos:] + nlist[:sl_end]
                slice_rev.reverse()
                nlist[pos:] = slice_rev[:len(nlist)-pos]
                nlist[:sl_end] = slice_rev[len(nlist)-pos:]
            else:
                nlist[pos:sl_end] = reversed(nlist[pos:sl_end])
            pos += length + skip_size
            while (pos >= len(nlist)):
                pos = pos - len(nlist)
            skip_size += 1
    sparse_list = []
    for i in range(0, len(nlist), 16):
        sparse_list.append(nlist[i:i+16])
    dense_list = []
    for sublist in sparse_list:
        xor_result = 0
        for element in sublist:
            xor_result = xor_result ^ element
        dense_list.append(xor_result)
    return "".join(["{:02x}".format(i) for i in dense_list])


def find_region(disk, row, col, already_done):
    if (disk[row][col] != "1"):
        return []
    positions = [(row, col)]
    if (row > 0):
        if ((row - 1, col) not in already_done):
            already_done.add((row - 1, col))
            positions += find_region(disk, row - 1, col, already_done)
    if (row < 127):
        if ((row + 1, col) not in already_done):
            already_done.add((row + 1, col))
            positions += find_region(disk, row + 1, col, already_done)
    if (col > 0):
        if ((row, col - 1) not in already_done):
            already_done.add((row, col - 1))
            positions += find_region(disk, row, col - 1, already_done)
    if (col < 127):
        if ((row, col + 1) not in already_done):
            already_done.add((row, col + 1))
            positions += find_region(disk, row, col + 1, already_done)
    return positions


def part1(puzzle_input):
    rows = [PUZZLE_INPUT + "-{}".format(i) for i in range(128)]
    hashes = [knot_hash(x) for x in rows]
    disk = ["".join([bin(int(x, base=16)).lstrip('-0b').zfill(4) for x in h])
            for h in hashes]
    return (sum([x.count("1") for x in disk]))


def part2(puzzle_input):
    rows = [PUZZLE_INPUT + "-{}".format(i) for i in range(128)]
    hashes = [knot_hash(x) for x in rows]
    disk = [list("".join([bin(int(x, base=16)).lstrip('-0b').zfill(4) for x in h]))
            for h in hashes]
    count = 0
    for row in range(128):
        for col in range(128):
            if (disk[row][col] == "1"):
                r = find_region(disk, row, col, set())
                for h in r:
                    disk[h[0]][h[1]] = None
                count += 1
    return count


print(part1(PUZZLE_INPUT))
print(part2(PUZZLE_INPUT))
