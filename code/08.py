"Hack it hack it."
from itertools import chain
from pathlib import Path


def get_letters(length_per_entry, length):
    return [k for k, v in length_per_entry.items() if v == length]


def get_numbers(entry):
    length_per_entry = {e: len(e) for e in sorted(entry)}
    length_per_number = {number: get_letters(length_per_entry, number) for number in range(10)}
    seven = length_per_number[3][0]
    one = length_per_number[2][0]
    eight = length_per_number[7][0]
    four = length_per_number[4][0]
    top_element = list(set(seven).difference(one))[0]
    middle_element = [
        char
        for char in set(eight).difference(one).difference(top_element)
        if all(char in five for five in length_per_number[5]) and not all(char in six for six in length_per_number[6])
    ][0]
    zero = [chars for chars in length_per_number[6] if middle_element not in chars][0]
    nine = [chars for chars in length_per_number[6] if all([x in chars for x in one]) and chars != zero][0]
    six = [chars for chars in length_per_number[6] if chars not in [nine, zero]][0]
    bottom_left = [char for char in zero if char not in nine and char in six][0]
    top_right = [char for char in zero if char in nine and char not in six][0]
    two = [
        option
        for option in length_per_number[5]
        if all([char in option for char in [top_element, top_right, bottom_left]])
    ][0]
    three = [
        option
        for option in length_per_number[5]
        if all([char in option for char in [top_right]]) and bottom_left not in option
    ][0]
    five = [option for option in length_per_number[5] if option not in [three, two]][0]
    return [zero, one, two, three, four, five, six, seven, eight, nine]


def get_output(numbers, four_digits):
    output_value = []
    for digit in four_digits:
        for idx, number in enumerate(numbers):
            if len(set(digit).symmetric_difference(set(number))) == 0:
                output_value.append(str(idx))
    return int("".join(output_value))


def part_one():
    return len(
        list(
            chain(
                *[
                    [
                        count
                        for number in entry.split("|")[1].strip().split(" ")
                        if (count := len(number)) in [2, 4, 3, 7]
                    ]
                    for entry in open(Path(__file__).parent.parent / "input" / "08.txt")
                ]
            )
        )
    )


def part_two():
    entries = [
        [f.strip().split(" ") for f in x.strip().split("|")]
        for x in open(Path(__file__).parent.parent / "input" / "08.txt")
    ]
    output_values = 0
    for entry in entries:
        numbers = get_numbers(entry[0])
        four_digits = entry[1]
        output_values += get_output(numbers, four_digits)
    return output_values


if __name__ == "__main__":
    print(f"Solution part one: {part_one()} \nSolution part two: {part_two()}")
