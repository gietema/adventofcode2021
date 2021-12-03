def part_1(data: list[int]):
    return len([y for x, y in zip(data[:-1], data[1:]) if x < y])


def part_2(data: list[int]):
    return len(
        [
            i
            for i, _ in enumerate(data)
            if sum(data[i : i + 3]) < sum(data[i + 1 : i + 4])
        ]
    )


if __name__ == "__main__":
    with open("day_01.txt", "r") as f:
        str_data = f.read().splitlines()
    input_data = [int(record) for record in str_data]

    answer_1 = part_1(input_data)
    print(answer_1)

    answer_2 = part_2(input_data)
    print(answer_2)
