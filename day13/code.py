#!/usr/bin/env python3
# -*- coding: utf-8 -*-


class FirewallLayer:
    def __init__(self, size):
        self.size = size
        self.scanner = 0
        self.downwards = True

    def forward(self):
        if (self.downwards):
            if (self.scanner < self.size - 1):
                self.scanner += 1
            else:
                self.downwards = False
                self.scanner -= 1
        else:
            if (self.scanner > 0):
                self.scanner -= 1
            else:
                self.downwards = True
                self.scanner += 1

    def after(self, iterations):
        s = self.scanner
        d = self.downwards
        for i in range(iterations):
            if d:
                if (s < self.size - 1):
                    s += 1
                else:
                    d = False
                    s -= 1
            else:
                if (s > 0):
                    s -= 1
                else:
                    d = True
                    s += 1
        return s


def part1(in_data):
    index = 0
    records = []
    for line in in_data.split("\n"):
        key = int(line.split(": ")[0])
        value = int(line.split(": ")[1])
        while (key > index):
            records.append(None)
            index += 1
        records.append(FirewallLayer(value))
        index += 1
    position = -1
    severity = 0
    for i in range(len(records)):
        position += 1
        if (records[position]):
            if (records[position].scanner == 0):
                severity += position * records[position].size
        for x in records:
            if x: x.forward()
    return severity


def part2(in_data):
    index = 0
    records = []
    for line in in_data.split("\n"):
        key = int(line.split(": ")[0])
        value = int(line.split(": ")[1])
        while (key > index):
            records.append(None)
            index += 1
        records.append(FirewallLayer(value))
        index += 1
        wait = 0
    while not all(records[i] is None
                  or records[i].after(i) != 0 for i in range(len(records))):
        # This will take some time
        for x in records:
            if x: x.forward()
        wait += 1
    return wait


with open("input.txt", "r") as in_file:
    in_data = in_file.read().strip()


print(part1(in_data))
print(part2(in_data))
