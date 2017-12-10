#!/usr/bin/env python3
# -*- coding: utf-8 -*-


def part1(in_data):
    nlist = list(range(0, 256))
    lengths = [int(x) for x in in_data.split(",")]
    pos = 0
    skip_size = 0
    for length in lengths:
        if (length > len(nlist)):
            continue
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
    return nlist[0] * nlist[1]


def part2(in_data):
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


with open("input.txt", "r") as in_file:
    in_data = in_file.read().strip()


print(part1(in_data))
print(part2(in_data))
