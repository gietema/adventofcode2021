from pathlib import Path

import numpy as np


def get_input():
    with open(str(Path(__file__).parent.parent / "input" / "04.txt")) as f:
        data = [line.rstrip() for line in f.readlines()]
    numbers = list(map(int, data[0].split(",")))
    data.append("")
    boards = []
    for idx, line in enumerate(data[1:]):
        if line == "":
            if idx > 0:
                boards[-1] = np.concatenate([boards[-1], boards[-1].T])
            boards.append(None)
        else:
            row = np.array([int(x) for x in line.split(" ") if x != ""])
            boards[-1] = np.array([row]) if boards[-1] is None else np.append(boards[-1], [row], axis=0)
    boards = np.array(boards[:-1])
    return numbers, boards


def part_one(numbers: list[int], boards: np.ndarray) -> int:
    for number in numbers:
        boards[boards == number] = -1
        if -5 in (board_sums := np.sum(boards, axis=2)):
            board_index = np.argwhere(board_sums == -5)[0][0]
            bingo_board = boards[board_index][:5]
            return bingo_board[bingo_board != -1].sum() * number


def part_two(numbers: list[int], boards: np.ndarray) -> int:
    winning_boards = []
    for number in numbers:
        boards[boards == number] = -1
        if -5 not in (board_sums := np.sum(boards, axis=2)):
            continue
        winning_board_indices = set(np.argwhere(board_sums == -5)[:, 0])
        if len(winning_board_indices) != len(boards):
            winning_boards.extend(winning_board_indices)
        else:
            board_idx = winning_board_indices.difference(winning_boards).pop()
            board = boards[board_idx][:5]
            return board[board != -1].sum() * number


if __name__ == "__main__":
    inp = get_input()
    print(f"Solution part one: {part_one(*inp)} \nSolution part two: {part_two(*inp)}")
