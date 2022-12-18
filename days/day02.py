from enum import Enum


class Move(Enum):
    ROCK = 1
    PAPER = 2
    SCISSORS = 3


def enum_match(letter):
    if letter == "A" or letter == "X":
        return Move.ROCK
    elif letter == "B" or letter == "Y":
        return Move.PAPER
    elif letter == "C" or letter == "Z":
        return Move.SCISSORS


def game_point(my_move, opponents_move):
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


input_day02 = open("../inputs/input_day02.txt").read()

games = input_day02.split("\n")
total_score = 0

for game in games:
    opponent = enum_match(game.split()[0])
    me = enum_match(game.split()[1])
    total_score += game_point(me, opponent)

print(total_score)
