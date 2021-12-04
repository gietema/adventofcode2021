def part_1(data: list[str]):

    bit_totals = [0] * len(data[0])
    for binary in data:
        bit_totals = [int(bit) + bit_totals[idx] for idx, bit in enumerate(binary)]

    gamma_bin = "".join([str(int(total > 500)) for total in bit_totals])
    epsilon_bin = gamma_bin.replace("1", "🎅").replace("0", "1").replace("🎅", "0")

    return int(gamma_bin, 2) * int(epsilon_bin, 2)


def _find_o2(data):
    index = 0
    while len(data) > 1:
        bit_numbers = [binary[index] for binary in data]
        one_idx = bit_numbers.index("1")
        if one_idx > len(data) / 2:
            data = data[:one_idx]  # keep zeros
        else:
            data = data[one_idx:]  # keep ones
        index += 1
    return int(data[0], 2)


def _find_co2(data):
    index = 0
    while len(data) > 1:
        bit_numbers = [binary[index] for binary in data]
        one_idx = bit_numbers.index("1")
        if one_idx <= len(data) / 2:
            data = data[:one_idx]  # keep zeros
        else:
            data = data[one_idx:]  # keep ones
        index += 1
    return int(data[0], 2)


def part_2(data: list[str]):
    data.sort()
    o2_rating = _find_o2(data.copy())
    co2_rating = _find_co2(data.copy())

    return o2_rating * co2_rating


if __name__ == "__main__":
    with open("day_03.txt", "r") as f:
        str_data = f.read().splitlines()

    answer_1 = part_1(str_data)
    print(answer_1)

    answer_2 = part_2(str_data)
    print(answer_2)
