import string
import re

input_day05 = open("inputs/input_day05.txt").read()
input_lines = input_day05.split("\n")

# create empty list of dictionaries for the input
crane = []
for i in range(9):
    crane.append({})

# setup input in dictionaries
for line_index, line in enumerate(input_lines[:8]):
    for i, char in enumerate(line):
        if line[i] in string.ascii_uppercase:
            crane[line_index].update({i: line[i]})

# create empty lists
crates = list()
crates2 = list()
for i in range(9):
    crates.append([])
    crates2.append([])

# add input to lists
for line in crane:
    for k, v in line.items():
        crates[k // 4].append(v)
        crates2[k // 4].append(v)

# arrangement for part 1
for line in input_lines[10:]:
    count = int(re.search("move (.*) from", line).group(1))
    from_crate = int(re.search("from (.*) to", line).group(1)) - 1
    to_crate = int(re.search("to (.*)", line).group(1)) - 1
    for _ in range(count):
        crates[to_crate].insert(0, crates[from_crate].pop(0))

# arrangement for part 2
for line in input_lines[10:]:
    count = int(re.search("move (.*) from", line).group(1))
    from_crate = int(re.search("from (.*) to", line).group(1)) - 1
    to_crate = int(re.search("to (.*)", line).group(1)) - 1
    temp = []
    for _ in range(count):
       temp.append(crates2[from_crate].pop(0))
    for crate in reversed(temp):
      crates2[to_crate].insert(0, crate)


# answer of part 1
for crate in crates:
    print(crate[0], end="")

print("")

# answer of part 2
for crate in crates2:
    print(crate[0], end="")