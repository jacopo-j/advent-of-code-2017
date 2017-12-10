#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import re


def cond_true(reg, operator, value):
    if (operator == ">="):
        return reg >= value
    elif (operator == "<="):
        return reg <= value
    elif (operator == "=="):
        return reg == value
    elif (operator == "<"):
        return reg < value
    elif (operator == ">"):
        return reg > value
    elif (operator == "!="):
        return reg != value


def part1(in_data):
    lines = in_data.split("\n")
    registers = {}
    regexp = ("([a-z]+) (inc|dec) (-?[0-9]+) if ([a-z]+) (>=|<=|==|<|>|!=) "
              "(-?[0-9]+)")
    for line in lines:
        instr = re.findall(regexp, line)[0]
        if (instr[0] not in registers):
            registers[instr[0]] = 0
        if (instr[3] not in registers):
            registers[instr[3]] = 0
        if (instr[1] == "inc"):
            variation = int(instr[2])
        elif (instr[1] == "dec"):
            variation = - int(instr[2])
        if cond_true(registers[instr[3]], instr[4], int(instr[5])):
            registers[instr[0]] += variation
    return registers[max(registers, key=lambda x: registers[x])]


def part2(in_data):
    lines = in_data.split("\n")
    registers = {}
    highest_value = 0
    regexp = ("([a-z]+) (inc|dec) (-?[0-9]+) if ([a-z]+) (>=|<=|==|<|>|!=) "
              "(-?[0-9]+)")
    for line in lines:
        instr = re.findall(regexp, line)[0]
        if (instr[0] not in registers):
            registers[instr[0]] = 0
        if (instr[3] not in registers):
            registers[instr[3]] = 0
        if (instr[1] == "inc"):
            variation = int(instr[2])
        elif (instr[1] == "dec"):
            variation = - int(instr[2])
        if cond_true(registers[instr[3]], instr[4], int(instr[5])):
            registers[instr[0]] += variation
        if (registers[instr[0]] > highest_value):
            highest_value = registers[instr[0]]
    return highest_value


with open("input.txt", "r") as in_file:
    in_data = in_file.read().strip()


print(part1(in_data))
print(part2(in_data))
