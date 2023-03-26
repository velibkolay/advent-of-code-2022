import string
import re

input_day05 = open("../inputs/input_day05.txt").read()

input_lines = input_day05.split("\n")
crane = []

for i in range(9):
    crane.append({})

for line_index, line in enumerate(input_lines[:8]):
    for i, char in enumerate(line):
        if line[i] in string.ascii_uppercase:
            crane[line_index].update({i: line[i]})

crates = []
for i in range(9):
    crates.append([])

for line in crane:
    for k, v in line.items():
        crates[k // 4].append(v)


print(crates)
print(input_lines[10])
print(re.search("from (.*) to", input_lines[10]).group(1))
