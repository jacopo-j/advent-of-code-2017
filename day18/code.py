#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from threading import Thread


def part1(in_data):
    instructions = in_data.split("\n")
    registers = {}
    cur = 0
    last_sound = None
    while (cur < len(instructions)):
        instr = instructions[cur]
        offset = 0
        r1 = instr.split(" ")[1]
        try:
            val1 = int(r1)
        except ValueError:
            if (r1 not in registers):
                registers[r1] = 0
            val1 = registers[r1]
        if (len(instr.split(" ")) > 2):
            r2 = instr.split(" ")[2]
            try:
                val2 = int(r2)
            except ValueError:
                if (r2 not in registers):
                    registers[r2] = 0
                val2 = registers[r2]
        op = instr.split(" ")[0]
        if (op == "snd"):
            last_sound = val1
        elif (op == "set"):
            registers[r1] = val2
        elif (op == "add"):
            registers[r1] += val2
        elif (op == "mul"):
            registers[r1] *= val2
        elif (op == "mod"):
            registers[r1] %= val2
        elif (op == "rcv" and last_sound != 0):
            return last_sound
        elif (op == "jgz" and val1 > 0):
            offset = val2 - 1
        cur += 1 + offset


def program(pid, instructions):
    global queue0, queue1
    global wait0, wait1
    global p1_count
    registers = {"p": pid}
    cur = 0
    while (cur < len(instructions)):
        instr = instructions[cur]
        offset = 0
        r1 = instr.split(" ")[1]
        try:
            val1 = int(r1)
        except ValueError:
            if (r1 not in registers):
                registers[r1] = 0
            val1 = registers[r1]
        if (len(instr.split(" ")) > 2):
            r2 = instr.split(" ")[2]
            try:
                val2 = int(r2)
            except ValueError:
                if (r2 not in registers):
                    registers[r2] = 0
                val2 = registers[r2]
        op = instr.split(" ")[0]
        if (op == "snd"):
            if (pid == 0):
                queue1.append(val1)
            elif (pid == 1):
                queue0.append(val1)
                p1_count += 1
        elif (op == "set"):
            registers[r1] = val2
        elif (op == "add"):
            registers[r1] += val2
        elif (op == "mul"):
            registers[r1] *= val2
        elif (op == "mod"):
            registers[r1] %= val2
        elif (op == "rcv"):
            if (pid == 0):
                q = queue0
            elif (pid == 1):
                q = queue1
            while (len(q) == 0):
                if wait0 > 10000000 and wait1 > 10000000:
                    return
                if (pid == 0):
                    wait0 += 1
                elif (pid == 1):
                    wait1 += 1
                continue
            if (pid == 0):
                wait0 = 0
            elif (pid == 1):
                wait1 = 0
            registers[r1] = q.pop(0)
        elif (op == "jgz" and val1 > 0):
            offset = val2 - 1
        cur += 1 + offset


def part2(in_data):
    global queue0, queue1
    global p1_count
    global wait0, wait1
    queue0 = []
    queue1 = []
    p1_count = 0
    wait0 = 0
    wait1 = 0
    instructions = in_data.split("\n")
    t0 = Thread(target=program, args=(0, instructions))
    t1 = Thread(target=program, args=(1, instructions))
    t0.start()
    t1.start()
    while (t0.isAlive() or t1.isAlive()):
        continue
    return p1_count


with open("input.txt", "r") as in_file:
    in_data = in_file.read().strip()


print(part1(in_data))
print(part2(in_data))
