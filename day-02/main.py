#!/usr/bin/env python

with open("input") as f:
    rounds = f.read().splitlines()

WIN = 6
LOSE = 0
DRAW = 3

shape_scores = { "X": 1, "Y": 2, "Z": 3 }
round_scores = {
    "X": { "A": DRAW, "B": LOSE, "C": WIN },
    "Y": { "A": WIN, "B": DRAW, "C": LOSE },
    "Z": { "A": LOSE, "B": WIN, "C": DRAW },
}

part1_total_score = 0
for round in rounds:
    opponent_shape, your_shape = round.split()
    part1_total_score += shape_scores[your_shape]
    part1_total_score += round_scores[your_shape][opponent_shape]
print(part1_total_score)

outcome_scores = { "X": LOSE, "Y": DRAW, "Z": WIN }
outcome_shapes = {
    "A": { "X": "Z", "Y": "X", "Z": "Y" },
    "B": { "X": "X", "Y": "Y", "Z": "Z" },
    "C": { "X": "Y", "Y": "Z", "Z": "X" }
}

part2_total_score = 0
for round in rounds:
    opponent_shape, outcome = round.split()
    part2_total_score += outcome_scores[outcome]
    your_shape = outcome_shapes[opponent_shape][outcome]
    part2_total_score += shape_scores[your_shape]
print(part2_total_score)
