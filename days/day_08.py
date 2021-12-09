from collections import Counter, defaultdict
from time import time


def part_1(data: list[str]):
    outputs = [line.split(" | ")[1] for line in data]
    counter = Counter()
    for output in outputs:
        digits = output.split(" ")
        nr_segments = [len(digit) for digit in digits]
        for number in nr_segments:
            counter[number] += 1

    target_nr_segments = [2, 3, 4, 7]
    return sum([counter[digit] for digit in target_nr_segments])


def part_2(data: list[str]):

    lines = [line.replace(" | ", " ") for line in data]

    outputs = [line.split(" | ")[1] for line in data]

    total = 0
    for line, output in zip(lines, outputs):
        digits = line.split(" ")
        digit_dict, loc_dict = _build_digit_dict(digits)

        pattern_dict = {}
        for digit, pattern in digit_dict.items():
            pattern_list = list(pattern)
            pattern_list.sort()
            pattern_str = "".join(pattern_list)
            pattern_dict[pattern_str] = str(digit)

        output_patterns = output.split(" ")

        digit_str_list = []
        for pattern in output_patterns:
            str_pattern = "".join(sorted(pattern))
            digit_str_list.append(pattern_dict[str_pattern])
        output_total = int("".join(digit_str_list))
        total += output_total

    return total


def _build_digit_dict(digits):
    digits_set = set(digits)
    size_dict = defaultdict(lambda: list())
    for digit in digits_set:
        size = len(digit)
        size_dict[size].append(set(digit))

    loc_dict = {"top": size_dict[3][0] - size_dict[2][0]}

    for digit in size_dict[6]:
        if bottom := set(digit) - size_dict[4][0] - loc_dict["top"]:
            if len(bottom) == 1:
                loc_dict["bottom"] = bottom
                break

    loc_dict["bottom_left"] = (
        size_dict[7][0] - loc_dict["top"] - loc_dict["bottom"] - size_dict[4][0]
    )

    digit_dict = {
        7: size_dict[3][0],
        1: size_dict[2][0],
        8: size_dict[7][0],
        4: size_dict[4][0],
        9: size_dict[7][0] - loc_dict["bottom_left"],
    }

    middle_three_set = {}
    for digit in size_dict[5]:
        middle_three_set = middle_three_set or digit_dict[8]
        middle_three_set = middle_three_set.intersection(digit)

    loc_dict["middle"] = middle_three_set - loc_dict["bottom"] - loc_dict["top"]
    digit_dict[3] = middle_three_set.union(digit_dict[1])

    loc_dict["top_left"] = digit_dict[8] - digit_dict[3] - loc_dict["bottom_left"]

    two_or_five_set = [
        candidate_set
        for candidate_set in size_dict[5]
        if candidate_set != digit_dict[3]
    ]  # and three
    digit_dict[5] = [
        five_set
        for five_set in two_or_five_set
        if five_set.intersection(loc_dict["top_left"])
    ][0]
    digit_dict[2] = [
        two_set
        for two_set in two_or_five_set
        if not two_set.intersection(loc_dict["top_left"])
    ][0]

    loc_dict["top_right"] = digit_dict[8] - digit_dict[5] - loc_dict["bottom_left"]
    loc_dict["bottom_right"] = digit_dict[8] - digit_dict[2] - loc_dict["top_left"]

    digit_dict[0] = digit_dict[8] - loc_dict["middle"]
    digit_dict[6] = digit_dict[8] - loc_dict["top_right"]
    return digit_dict, loc_dict


def _build_easy_options_dict(digits: list[str]):
    options_dict = {}
    nr_segments = [len(digit) for digit in digits]
    if 2 in nr_segments:  # 1
        idx = nr_segments.index(2)
        options_dict[1] = set(digits[idx])
    if 3 in nr_segments:  # 7
        idx = nr_segments.index(3)
        options_dict[7] = set(digits[idx])
    if 4 in nr_segments:  # 4
        idx = nr_segments.index(4)
        options_dict[4] = set(digits[idx])
    if 7 in nr_segments:  # 8
        idx = nr_segments.index(7)
        options_dict[8] = set(digits[idx])
    return options_dict


if __name__ == "__main__":
    with open("day_08.txt", "r") as f:
        input_data = f.read().splitlines()

    answer_1 = part_1(input_data)
    print(answer_1)
    start = time()
    answer_2 = part_2(input_data)
    end = time()
    print(answer_2)
