def is_contains(f_start: int, f_end: int, s_start: int, s_end: int):
    if f_start <= s_start and f_end >= s_end:
        return True
    elif s_start <= f_start and s_end >= f_end:
        return True
    else:
        return False


def is_overlaps(f_start: int, f_end: int, s_start: int, s_end: int):
    if f_start < s_start:
        if f_end >= s_start:
            return True
        else:
            return False
    elif s_start < f_start:
        if s_end >= f_start:
            return True
        else:
            return False
    else:
        return True


input_day04 = open("../inputs/input_day04.txt").read()
assignment_pairs = input_day04.split("\n")
sum_contains = 0
sum_overlaps = 0

for assignment_pair in assignment_pairs:
    first_assignment, second_assignment = assignment_pair.split(",")
    first_start, first_end = str(first_assignment).split("-")
    second_start, second_end = str(second_assignment).split("-")
    if is_contains(int(first_start), int(first_end), int(second_start), int(second_end)):
        sum_contains += 1
    if is_overlaps(int(first_start), int(first_end), int(second_start), int(second_end)):
        sum_overlaps += 1

print(sum_contains)
print(sum_overlaps)
