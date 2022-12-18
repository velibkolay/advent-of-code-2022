input_day1 = open("../inputs/input_day01.txt").read()

elves = input_day1.split("\n\n")

elves_calories = []


for elf in elves:
    calories = elf.split("\n")
    sum_calorie = 0
    for calorie in calories:
        sum_calorie += int(calorie)
    elves_calories.append(sum_calorie)

print(elves_calories)
print(max(elves_calories))
print(elves_calories.index(max(elves_calories)))
print(elves_calories.index(54273))

elves_calories.sort(reverse=True)
print(elves_calories[0])
print(elves_calories[1])
print(elves_calories[2])
print(sum(elves_calories[0:3]))