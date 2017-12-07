#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import re


def get_total_weight(programs, index, weight=0):
    if (len(programs[index]["children"]) == 0):
        return weight + programs[index]["weight"]
    for child in programs[index]["children"]:
        child_index = programs.index(
            [x for x in programs if x["parent"] == child][0])
        weight = get_total_weight(programs, child_index, weight)
    return weight + programs[index]["weight"]


def part1(in_data):
    programs = {}
    rexp = "([a-z]+) \([0-9]+\)(?: -> ([a-z ,]+))*"
    for line in in_data.split("\n"):
        parent, children = re.findall(rexp, line)[0]
        if (children == ""):
            children = []
        else:
            children = children.split(", ")
        programs[parent] = children
    all_children = []
    for c in programs.values():
        all_children += c
    for parent, children in programs.items():
        if (len(children) > 0):
            if all(x != parent for x in all_children):
                return parent


def part2(in_data):
    programs = []
    rexp = "([a-z]+) \(([0-9]+)\)(?: -> ([a-z ,]+))*"
    for line in in_data.split("\n"):
        parent, weight, children = re.findall(rexp, line)[0]
        if (children == ""):
            children = []
        else:
            children = children.split(", ")
        programs.append({"parent": parent,
                         "weight": int(weight),
                         "children": children})
    root_parent = part1(in_data)
    root_idx = programs.index(
        [x for x in programs if x["parent"] == root_parent][0])
    current_program = programs[root_idx]
    while (len(current_program["children"]) > 0):
        children_weights = []
        for child in current_program["children"]:
            children_weights.append(get_total_weight(
                programs,
                programs.index(
                    [x for x in programs if x["parent"] == child][0])))
        odd_one_out = None
        for w in children_weights:
            if (children_weights.count(w) == 1):
                odd_one_out = w
            elif (children_weights.count(w) > 1):
                cur_correct_weight = w
        if (odd_one_out is None):
            for cw in children_weights:
                last_correct_weight -= cw
            return last_correct_weight
        else:
            ooo_child_idx = children_weights.index(odd_one_out)
            ooo_child_name = current_program["children"][ooo_child_idx]
            cur_idx = programs.index(
                [x for x in programs if x["parent"] == ooo_child_name][0])
            last_correct_weight = cur_correct_weight
            current_program = programs[cur_idx]


with open("input.txt", "r") as in_file:
    in_data = in_file.read().strip()


print(part1(in_data))
print(part2(in_data))
