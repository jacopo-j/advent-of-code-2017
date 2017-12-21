#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import re
from collections import defaultdict


class Particle:
    def __init__(self, num):
        self.pos = [int(x) for x in num[:3]]
        self.vel = [int(x) for x in num[3:6]]
        self.acc = [int(x) for x in num[6:]]

    def tick(self):
        self.vel[0] += self.acc[0]
        self.vel[1] += self.acc[1]
        self.vel[2] += self.acc[2]
        self.pos[0] += self.vel[0]
        self.pos[1] += self.vel[1]
        self.pos[2] += self.vel[2]

    def distance(self):
        return abs(self.pos[0]) + abs(self.pos[1]) + abs(self.pos[2])

    def get_pos(self):
        return (self.pos[0], self.pos[1], self.pos[2])


def list_duplicates(particles):
    done = defaultdict(list)
    for i, prt in enumerate(particles):
        done[prt].append(i)
    return [x for x, y in done.items() if len(y) > 1]


def part1(in_data):
    particles = []
    for line in in_data.split("\n"):
        particles.append(Particle(re.findall(
            ("p=<(-?[0-9]+),(-?[0-9]+),(-?[0-9]+)>, "
             "v=<(-?[0-9]+),(-?[0-9]+),(-?[0-9]+)>, "
             "a=<(-?[0-9]+),(-?[0-9]+),(-?[0-9]+)>"), line)[0]))
    distances = [0] * len(particles)
    for _ in range(500):
        for idx, p in enumerate(particles):
            p.tick()
            distances[idx] = p.distance()
    return distances.index(min([x.distance() for x in particles]))


def part2(in_data):
    particles = []
    for line in in_data.split("\n"):
        particles.append(Particle(re.findall(
            ("p=<(-?[0-9]+),(-?[0-9]+),(-?[0-9]+)>, "
             "v=<(-?[0-9]+),(-?[0-9]+),(-?[0-9]+)>, "
             "a=<(-?[0-9]+),(-?[0-9]+),(-?[0-9]+)>"), line)[0]))
    for _ in range(500):
        for p in particles:
            p.tick()
        collisions = list_duplicates([x.get_pos() for x in particles])
        for i in collisions:
            particles = [x for x in particles if x.get_pos() != i]
    return len(particles)


with open("input.txt", "r") as in_file:
    in_data = in_file.read().strip()


print(part1(in_data))
print(part2(in_data))
