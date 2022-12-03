#!/usr/bin/env python

with open("input") as f:
    amounts = [sum(map(int, s.split('\n'))) for s in f.read().split('\n\n')]
    
print(max(amounts))
print(sum(sorted(amounts)[-3:]))