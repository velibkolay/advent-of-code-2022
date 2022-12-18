from enum import IntEnum


class Move(IntEnum):
    ROCK = 1
    PAPER = 2
    SCISSORS = 3


class Result(IntEnum):
    WIN = 6
    DRAW = 3
    LOSE = 0


def enum_match(letter):
    if letter == "A" or letter == "X":
        return Move.ROCK
    elif letter == "B" or letter == "Y":
        return Move.PAPER
    elif letter == "C" or letter == "Z":
        return Move.SCISSORS


def result_match(letter):
    if letter == "Z":
        return Result.WIN
    elif letter == "Y":
        return Result.DRAW
    else:
        return Result.LOSE


def game_point_move(my_move: Move, opponents_move: Move):
    if my_move == Move.ROCK:
        if opponents_move == Move.PAPER:
            return 0 + 1
        if opponents_move == Move.ROCK:
            return 3 + 1
        if opponents_move == Move.SCISSORS:
            return 6 + 1
    elif my_move == Move.PAPER:
        if opponents_move == Move.SCISSORS:
            return 0 + 2
        if opponents_move == Move.PAPER:
            return 3 + 2
        if opponents_move == Move.ROCK:
            return 6 + 2
    elif my_move == Move.SCISSORS:
        if opponents_move == Move.ROCK:
            return 0 + 3
        if opponents_move == Move.SCISSORS:
            return 3 + 3
        if opponents_move == Move.PAPER:
            return 6 + 3
    else:
        return 0


def game_point_result(opponents_move: Move, result: Result):
    if opponents_move == Move.ROCK:
        if result == Result.WIN:
            return Move.PAPER + Result.WIN
        elif result == Result.DRAW:
            return Move.ROCK + Result.DRAW
        else:
            return Move.SCISSORS + Result.LOSE
    elif opponents_move == Move.PAPER:
        if result == Result.WIN:
            return Move.SCISSORS + Result.WIN
        elif result == Result.DRAW:
            return Move.PAPER + Result.DRAW
        else:
            return Move.ROCK + Result.LOSE
    else:
        if result == Result.WIN:
            return Move.ROCK + Result.WIN
        elif result == Result.DRAW:
            return Move.SCISSORS + Result.DRAW
        else:
            return Move.PAPER + Result.LOSE


input_day02 = open("../inputs/input_day02.txt").read()

games = input_day02.split("\n")
total_score_part1 = 0
total_score_part2 = 0

for game in games:
    opponent = enum_match(game.split()[0])
    me = enum_match(game.split()[1])
    total_score_part1 += game_point_move(my_move=me, opponents_move=opponent)
    total_score_part2 += game_point_result(opponents_move=opponent, result=result_match(game.split()[1]))

print(f"Day 02, Part 1: {total_score_part1}")
print(f"Day 02, Part 2: {total_score_part2}")
