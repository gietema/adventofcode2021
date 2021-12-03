from typing import List


def get_moves() -> List[List[str]]:
    with open("day_02.txt", "r") as f:
        return [line.rstrip().split(" ") for line in f.readlines()]


def part_one() -> int:
    hor_pos, depth = 0, 0
    for move in get_moves():
        move_type, move = move[0], int(move[1])
        match move_type:
            case "forward":
                hor_pos += move
            case "down":
                depth += move
            case "up":
                depth -= move
    return hor_pos * depth


def part_two() -> int:
    hor_pos, depth, aim = 0, 0, 0
    for move in get_moves():
        move_type, move = move[0], int(move[1])
        move = int(move)
        match move_type:
            case "forward":
                hor_pos += move
                depth += (aim * move)
            case "down":
                aim += move
            case "up":
                aim -= move
    return hor_pos * depth


if __name__ == "__main__":
    print(f"Solution part one: {part_one()} \nSolution part two: {part_two()}")
