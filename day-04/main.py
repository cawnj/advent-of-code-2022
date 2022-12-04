#!/usr/bin/env python

with open("input") as f:
    pairs = f.read().splitlines()

part1_total = 0
part2_total = 0
for pair in pairs:
    first_start, first_end, second_start, second_end = map(int, pair.replace(",", "-").split("-"))
    first_assignment = set(range(first_start, first_end+1))
    second_assignment = set(range(second_start, second_end+1))
    if first_assignment.issubset(second_assignment) or second_assignment.issubset(first_assignment):
        part1_total += 1
    if first_assignment & second_assignment:
        part2_total += 1
print(part1_total)
print(part2_total)
