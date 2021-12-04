from pathlib import Path


def get_input() -> list[list[str]]:
    with open(str(Path(__file__).parent.parent / "input" / "02.txt")) as f:
        return [line.rstrip().split(" ") for line in f.readlines()]


def part_one(moves: list[list[str]]) -> int:
    hor_pos, depth = 0, 0
    for move in moves:
        move_type, move = move[0], int(move[1])
        match move_type:
            case "forward":
                hor_pos += move
            case "down":
                depth += move
            case "up":
                depth -= move
    return hor_pos * depth


def part_two(moves: list[list[str]]) -> int:
    hor_pos, depth, aim = 0, 0, 0
    for move in moves:
        move_type, move = move[0], int(move[1])
        match move_type:
            case "forward":
                hor_pos += move
                depth += aim * move
            case "down":
                aim += move
            case "up":
                aim -= move
    return hor_pos * depth


if __name__ == "__main__":
    inp = get_input()
    print(f"Solution part one: {part_one(inp)} \nSolution part two: {part_two(inp)}")
