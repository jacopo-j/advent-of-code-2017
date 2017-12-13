#!/usr/bin/env python3
# -*- coding: utf-8 -*-


def count_tree(elements, links, count=1, already_done=["0"]):
    for element in elements:
        if (element in already_done):
            continue
        count += 1
        already_done.append(element)
        count = count_tree(links[element], links, count, already_done)
    return count


def get_full_tree(element, links, tree=[]):
    if element not in tree:
        tree.append(element)
    for value in links[element]:
        if value in tree:
            continue
        tree.append(value)
        tree = get_full_tree(value, links, tree)
    return tree


def part1(in_data):
    links = {}
    for line in in_data.split("\n"):
        parent = line.split(" <-> ")[0]
        children = line.split(" <-> ")[1].split(", ")
        if (parent not in links):
            links[parent] = []
        for child in children:
            links[parent].append(child)
    return count_tree(links["0"], links)


def part2(in_data):
    links = {}
    for line in in_data.split("\n"):
        parent = line.split(" <-> ")[0]
        children = line.split(" <-> ")[1].split(", ")
        if (parent not in links):
            links[parent] = []
        for child in children:
            links[parent].append(child)
    count = 0
    for key in list(links.keys()):
        if key not in links:
            continue
        full_tree = get_full_tree(key, links)
        for i in full_tree:
            links.pop(i, None)
        count += 1
    return count


with open("input.txt", "r") as in_file:
    in_data = in_file.read().strip()


print(part1(in_data))
print(part2(in_data))
