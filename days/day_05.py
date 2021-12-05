from collections import Counter
from dataclasses import dataclass


@dataclass
class VentLine:
    x1: int
    x2: int
    y1: int
    y2: int

    def path(self, check_diagonal: bool = False):
        if path := self.horizontal_path:
            return path
        elif path := self.vertical_path:
            return path
        elif check_diagonal and (path := self.diagonal_path):
            return path
        return []

    @property
    def horizontal_path(self):
        if self.y1 == self.y2:
            min_x = min([self.x1, self.x2])
            max_x = max([self.x1, self.x2])
            return [(x, self.y1) for x in range(min_x, max_x + 1)]
        return []

    @property
    def vertical_path(self):
        if self.x1 == self.x2:
            min_y = min([self.y1, self.y2])
            max_y = max([self.y1, self.y2])
            return [(self.x1, y) for y in range(min_y, max_y + 1)]
        return []

    @property
    def diagonal_path(self):
        diag_up = self.x2 - self.x1 == self.y2 - self.y1
        diag_down = self.x2 - self.x1 == self.y1 - self.y2

        min_x = min([self.x1, self.x2])
        max_x = max([self.x1, self.x2])
        min_y = min([self.y1, self.y2])
        max_y = max([self.y1, self.y2])

        if diag_up:
            # 1,1 -> 3,3 covers points 1,1, 2,2, and 3,3
            return [
                (x, y) for x, y in zip(range(min_x, max_x + 1), range(min_y, max_y + 1))
            ]
        if diag_down:
            # 9,7 -> 7,9 covers points 9,7, 8,8, and 7,9
            return [
                (x, y)
                for x, y in zip(
                    reversed(range(min_x, max_x + 1)), range(min_y, max_y + 1)
                )
            ]
        return []


def read_vent_lines(data: list[str]) -> list[VentLine]:
    vent_lines = []
    for record in data:
        x1, middle, y2 = record.split(",")
        y1, x2 = middle.split(" -> ")
        vent_tuple = tuple(map(int, (x1, x2, y1, y2)))
        vent_line = VentLine(*vent_tuple)
        vent_lines.append(vent_line)
    return vent_lines


def part_1(data: list[str]):

    vent_lines = read_vent_lines(data)

    coord_counter = Counter()
    for vent_line in vent_lines:
        for coord in vent_line.path():
            coord_counter[coord] += 1

    more_than_once = {x: count for x, count in coord_counter.items() if count > 1}
    return len(more_than_once)


def part_2(data: list[str]):
    vent_lines = read_vent_lines(data)

    coord_counter = Counter()
    for vent_line in vent_lines:
        for coord in vent_line.path(check_diagonal=True):
            coord_counter[coord] += 1

    more_than_once = {x: count for x, count in coord_counter.items() if count > 1}
    return len(more_than_once)


if __name__ == "__main__":
    with open("day_05.txt", "r") as f:
        input_data = f.read().splitlines()

    answer_1 = part_1(input_data)
    print(answer_1)

    answer_2 = part_2(input_data)
    print(answer_2)
