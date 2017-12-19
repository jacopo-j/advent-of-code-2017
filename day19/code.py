#!/usr/bin/env python3
# -*- coding: utf-8 -*-


with open("input.txt", "r") as in_file:
    in_data = in_file.read()


matrix = [list(x) for x in in_data.split("\n") if x.strip() != ""]
x = matrix[0].index("|")
y = 0
direction = "d"
string = ""
steps = 0
while True:
    if (direction == "d"):
        while (matrix[y][x] not in ("+", " ")):
            if (matrix[y][x].isalpha()): string += matrix[y][x]
            y += 1
            steps += 1
        if (matrix[y][x] == " "): break
        steps += 1
        if ((x + 1) < len(matrix[y]) and matrix[y][x + 1] != " "):
            direction = "r"
            x += 1
        else:
            direction = "l"
            x -= 1
    elif (direction == "u"):
        while (matrix[y][x] not in ("+", " ")):
            if (matrix[y][x].isalpha()): string += matrix[y][x]
            y -= 1
            steps += 1
        if (matrix[y][x] == " "): break
        steps += 1
        if ((x + 1) < len(matrix[y]) and matrix[y][x + 1] != " "):
            direction = "r"
            x += 1
        else:
            direction = "l"
            x -= 1
    elif (direction == "l"):
        while (matrix[y][x] not in ("+", " ")):
            if (matrix[y][x].isalpha()): string += matrix[y][x]
            x -= 1
            steps += 1
        if (matrix[y][x] == " "): break
        steps += 1
        if ((y + 1) < len(matrix) and matrix[y + 1][x] != " "):
            direction = "d"
            y += 1
        else:
            direction = "u"
            y -= 1
    elif (direction == "r"):
        while (matrix[y][x] not in ("+", " ")):
            if (matrix[y][x].isalpha()): string += matrix[y][x]
            x += 1
            steps += 1
        if (matrix[y][x] == " "): break
        steps += 1
        if ((y + 1) < len(matrix) and matrix[y + 1][x] != " "):
            direction = "d"
            y += 1
        else:
            direction = "u"
            y -= 1


print(string)
print(steps)
