from collections import Counter
from typing import Union


def part_1(fishies: list[int]):
    for day in range(80):
        fishies = _wait_a_day(fishies)
        fishies.sort()
        if nr_pregnant_fishies := fishies.count(-1):
            fishies[:nr_pregnant_fishies] = [6] * nr_pregnant_fishies
            new_fishies = [8] * nr_pregnant_fishies
            fishies += new_fishies
    return len(fishies)


def part_2(fishies: list[int]):
    fishies = Counter(fishies)

    for day in range(256):
        fishies = _wait_a_day(fishies)
        if (nr_pregnant_fishies := fishies[-1]) > 0:
            fishies.pop(-1)
            fishies[6] += nr_pregnant_fishies
            fishies[8] = nr_pregnant_fishies
    return sum(fishies.values())


def _wait_a_day(fishies: Union[list | Counter]):
    if isinstance(fishies, list):
        return [fish - 1 for fish in fishies]
    if isinstance(fishies, Counter):
        new_counter = Counter()
        for old_count, nr_fish in fishies.items():
            new_counter[old_count - 1] = nr_fish
        return new_counter
    raise TypeError


if __name__ == "__main__":
    with open("day_06.txt", "r") as f:
        input_data = list(map(int, f.read().split(",")))

    answer_1 = part_1(input_data)
    print(answer_1)

    answer_2 = part_2(input_data)
    print(answer_2)
