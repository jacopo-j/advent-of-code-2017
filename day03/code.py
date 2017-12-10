#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import numpy


PUZZLE_INPUT = 277678


def part2_value(matrix, pos):
    possible_positions = ((pos[1] - 1, pos[0] - 1),
                          (pos[1], pos[0] - 1),
                          (pos[1] - 1, pos[0]),
                          (pos[1] - 1, pos[0] + 1),
                          (pos[1] + 1, pos[0] - 1),
                          (pos[1] + 1, pos[0]),
                          (pos[1], pos[0] + 1),
                          (pos[1] + 1, pos[0] + 1))
    value = 0
    for i in possible_positions:
        try:
            value += (matrix[i[0]][i[1]] or 0)
        except IndexError:
            pass
    return value


def part1(puzzle_input):
    # First of all, we need to determine the smallest size of a spiral
    # matrix which contains the input number. A spiral matrix with
    # origin in its center contains all the natural numbers from 0 to
    # n^2 where n is its dimension. Our spiral matrix must be
    # symmetrical around 1, which means we cannot have a matrix with an
    # even dimension. So, are going to create a matrix whose dimension
    # is the odd integer value next to the square root of the input
    # number.
    matrix_size = int(numpy.ceil(numpy.sqrt(puzzle_input)))
    if (matrix_size % 2 == 0):
        matrix_size += 1

    # Build a square matrix having these dimensions
    matrix = []
    for _ in range(0, matrix_size):
        matrix.append([None] * matrix_size)

    # Populate the spiral matrix
    pos = [int(matrix_size / 2), int(matrix_size / 2)]
    matrix[pos[1]][pos[0]] = 1
    value = 2
    right_moves = 1
    up_moves = 1
    left_moves = 2
    down_moves = 2
    while (0 <= pos[0] < matrix_size) and (0 <= pos[1] < matrix_size):
        try:
            for _ in range(0, right_moves):
                pos[0] += 1
                matrix[pos[1]][pos[0]] = value
                value += 1
            right_moves += 2
            for _ in range(0, up_moves):
                pos[1] -= 1
                matrix[pos[1]][pos[0]] = value
                value += 1
            up_moves += 2
            for _ in range(0, left_moves):
                pos[0] -= 1
                matrix[pos[1]][pos[0]] = value
                value += 1
            left_moves += 2
            for _ in range(0, down_moves):
                pos[1] += 1
                matrix[pos[1]][pos[0]] = value
                value += 1
            down_moves += 2
        except IndexError:
            break

    # Find the position of the input number inside the matrix
    input_pos = [(index, row.index(puzzle_input))
                 for index, row in enumerate(matrix)
                 if puzzle_input in row][0]

    # Return the Manhattan distance between the position of the input
    # number and the center of the matrix
    return (abs(input_pos[1] - int(matrix_size / 2))
            + abs(input_pos[0] - int(matrix_size / 2)))


def part2(puzzle_input):
    # This time determining the minimum size of a useful matrix is not
    # possible. We'll try with a 3x3 matrix first, and if the matrix is
    # too small we'll try again with a larger matrix.
    matrix_size = 3

    while True:
        matrix = []
        for _ in range(0, matrix_size):
            matrix.append([None] * matrix_size)

        # Populate the spiral matrix
        pos = [int(matrix_size / 2), int(matrix_size / 2)]
        matrix[pos[1]][pos[0]] = 1
        right_moves = 1
        up_moves = 1
        left_moves = 2
        down_moves = 2
        while (0 <= pos[0] < matrix_size) and (0 <= pos[1] < matrix_size):
            try:
                for _ in range(0, right_moves):
                    pos[0] += 1
                    matrix[pos[1]][pos[0]] = part2_value(matrix, pos)
                right_moves += 2
                for _ in range(0, up_moves):
                    pos[1] -= 1
                    matrix[pos[1]][pos[0]] = part2_value(matrix, pos)
                up_moves += 2
                for _ in range(0, left_moves):
                    pos[0] -= 1
                    matrix[pos[1]][pos[0]] = part2_value(matrix, pos)
                left_moves += 2
                for _ in range(0, down_moves):
                    pos[1] += 1
                    matrix[pos[1]][pos[0]] = part2_value(matrix, pos)
                down_moves += 2
            except IndexError:
                break

        # Determine numbers bigger than puzzle_input
        bigger_numbers = []
        for row in matrix:
            for number in row:
                if (number > puzzle_input):
                    bigger_numbers.append(number)

        # Check if the matrix was too small
        if (len(bigger_numbers) == 0):
            matrix_size += 2
        else:
            break

    return min(bigger_numbers)


print(part1(PUZZLE_INPUT))
print(part2(PUZZLE_INPUT))
