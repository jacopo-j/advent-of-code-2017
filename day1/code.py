#!/usr/bin/env python3
# -*- coding: utf-8 -*-


def part1(in_data):
    n_sum = 0
    for i in range(0, len(in_data) - 1):
        if (in_data[i] == in_data[i + 1]):
            n_sum += int(in_data[i])
        i += 1
    if (in_data[-1] == in_data[0]):
        n_sum += int(in_data[-1])
    return n_sum


def part2(in_data):
    n_sum = 0
    list_length = len(in_data)
    for i in range(0, list_length):
        check_index = i + int(list_length / 2)
        if (check_index >= list_length):
            check_index = check_index - list_length
        if (in_data[i] == in_data[check_index]):
            n_sum += int(in_data[i])
        i += 1
    return n_sum


with open("input.txt", "r") as input_file:
    in_data = input_file.read().strip()


print(part1(in_data))
print(part2(in_data))