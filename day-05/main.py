#!/usr/bin/env python

with open("input") as f:
    stack_lines, op_lines = f.read().split("\n\n")

num_columns = int(stack_lines.splitlines()[-1].split()[-1])
stacks = [[] for i in range(num_columns)]

for line in stack_lines.splitlines()[:-1][::-1]:
    for i in range(num_columns):
        crate = line[i*4+1]
        if crate.isalpha():
            stacks[i].append(crate)

for line in op_lines.splitlines():
    move_amount, from_pos, to_pos = [int(x) for x in line.split()[1::2]]
    for i in range(move_amount):
        crate = stacks[from_pos-1].pop()
        stacks[to_pos-1].append(crate)

part1_answer = ''.join([stack[-1] for stack in stacks])
print(part1_answer)


num_columns = int(stack_lines.splitlines()[-1].split()[-1])
stacks = [[] for i in range(num_columns)]

for line in stack_lines.splitlines()[:-1][::-1]:
    for i in range(num_columns):
        crate = line[i*4+1]
        if crate.isalpha():
            stacks[i].append(crate)

for line in op_lines.splitlines():
    move_amount, from_pos, to_pos = [int(x) for x in line.split()[1::2]]
    crates_to_move = stacks[from_pos-1][-move_amount:]
    stacks[from_pos-1] = stacks[from_pos-1][:-move_amount]
    stacks[to_pos-1] += crates_to_move

part2_answer = ''.join([stack[-1] for stack in stacks])
print(part2_answer)
