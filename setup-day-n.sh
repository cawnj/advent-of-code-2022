#!/bin/sh

# mkdir
n=`printf %02d $1`
mkdir day-$n

# init main.py
echo "#!/usr/bin/env python\n" > day-$n/main.py

# get cookie and download input
export $(xargs < .env)
curl "https://adventofcode.com/2022/day/$1/input" -H "cookie: $cookie" -o day-$n/input

# open task
open -a "Google Chrome" "https://adventofcode.com/2022/day/$1"

