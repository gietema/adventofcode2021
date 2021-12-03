def part_1(data: list[str]):

    horizontal_move = sum(
        [int(move.replace("forward ", "")) for move in data if move.startswith("f")]
    )

    down_move = sum(
        [int(move.replace("down ", "")) for move in data if move.startswith("d")]
    )
    up_move = sum(
        [int(move.replace("up ", "")) for move in data if move.startswith("u")]
    )

    return (down_move - up_move) * horizontal_move


def part_2(data: list[str]):
    aim = 0
    depth = 0
    horizon = 0
    for move in data:
        if move.startswith(text_to_replace := "forward "):
            horizon += (amount := int(move.replace(text_to_replace, "")))
            depth += amount * aim
        elif move.startswith(text_to_replace := "down "):
            aim += int(move.replace(text_to_replace, ""))
        elif move.startswith(text_to_replace := "up "):
            aim -= int(move.replace(text_to_replace, ""))
    return horizon * depth


if __name__ == "__main__":
    with open("day_02.txt", "r") as f:
        str_data = f.read().splitlines()

    answer_1 = part_1(str_data)
    print(answer_1)

    answer_2 = part_2(str_data)
    print(answer_2)
