from pathlib import Path

CHAR_DICT = {"[": "]", "(": ")", "<": ">", "{": "}"}
SCORE_DICT_PART_TWO = {")": 1, "]": 2, "}": 3, ">": 4}


def part_one(subsystem: list[str]) -> int:
    score_dict = {"]": 57, "}": 1197, ")": 3, ">": 25137}
    score = 0
    for line in subsystem:
        expected_closes = []
        for char in line:
            if char in CHAR_DICT:
                expected_closes.append(CHAR_DICT[char])
            elif char == expected_closes[-1]:
                expected_closes.pop()
            else:
                score += score_dict[char]
                break
    return score


def score_line(closes: list[str]) -> int:
    score = 0
    for char in closes:
        score *= 5
        score += SCORE_DICT_PART_TWO[char]
    return score


def part_two(subsystem: list[str]) -> int:
    scores = []
    for line in subsystem:
        expected_closes, found_error = [], False
        for char in line:
            if char in CHAR_DICT:
                expected_closes.append(CHAR_DICT[char])
            elif char == expected_closes[-1]:
                expected_closes.pop()
            else:
                found_error = True
        if len(expected_closes) > 0 and not found_error:
            scores.append(score_line(expected_closes[::-1]))
    return sorted(scores)[len(scores) // 2]


if __name__ == "__main__":
    inp = [line.rstrip() for line in open(Path(__file__).parent.parent / "input" / "10.txt")]
    print(f"Solution part one: {part_one(inp)} \nSolution part two: {part_two(inp)}")
