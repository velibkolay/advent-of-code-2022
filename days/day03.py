import numpy as np

def get_priority(char: str):
    if char.isupper():
        return ord(char) - 38
    else:
        return ord(char) - 96


input_day03 = open("../inputs/input_day03.txt").read()

rucksacks = input_day03.split("\n")
sum_priority = 0

for rucksack in rucksacks:
    first_part, second_part = rucksack[:len(rucksack) // 2], rucksack[len(rucksack) // 2:]
    intersection = set(first_part).intersection(second_part)
    sum_priority += get_priority(intersection.pop())

print(sum_priority)

# part 2

sum_priority_group = 0

# three-elf group
groups = list(zip(*(iter(rucksacks),) * 3))

for group in groups:
    intersection = set(group[0]).intersection(group[1]).intersection(group[2])
    sum_priority_group += get_priority(intersection.pop())

print(sum_priority_group)