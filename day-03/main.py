#!/usr/bin/env python

with open("input") as f:
    rucksacks = f.read().splitlines()

priorities = " abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"

part1_total = 0
for rucksack in rucksacks:
    mid = len(rucksack) // 2
    first_compartment, second_compartment = rucksack[:mid], rucksack[mid:]
    common_item = str(*(set(first_compartment) & set(second_compartment)))
    part1_total += priorities.index(common_item)
print(part1_total)

part2_total = 0
for i in range(0, len(rucksacks), 3):
    group = rucksacks[i:i+3]
    common_item = str(*(set(group[0]) & set(group[1]) & set(group[2])))
    part2_total += priorities.index(common_item)
print(part2_total)
