from math import prod
from time import time


def part_1(heigth_map: list[str]):
    map_checker = MapChecker(heigth_map=heigth_map)
    low_points = map_checker.find_low_points()
    return map_checker.score_low_points(low_points)


class MapChecker:
    def __init__(self, heigth_map: list[str]):
        self.height_map = heigth_map
        self.last_row = len(heigth_map) - 1
        self.last_column = len(heigth_map[0]) - 1

    def score_low_points(self, low_points: list[tuple]):
        total_risk = 0
        for point in low_points:
            row, column = point
            total_risk += int(self.height_map[row][column]) + 1
        return total_risk

    def find_low_points(self):
        low_points = []
        for row, line in enumerate(self.height_map):
            for column, point in enumerate(line):
                is_low_point = all(
                    [
                        self._is_lower_than_left(line, column),
                        self._is_lower_than_right(line, column),
                        self._is_lower_than_top(row, column),
                        self._is_lower_than_bottom(row, column),
                    ]
                )
                if is_low_point:
                    low_points.append((row, column))
        return low_points

    @staticmethod
    def _is_lower_than_left(line, column):
        if column == 0:
            return True
        return int(line[column]) < int(line[column - 1])

    def _is_lower_than_right(self, line, column):
        if column == self.last_column:
            return True
        return int(line[column]) < int(line[column + 1])

    def _is_lower_than_top(self, row, column):
        if row == 0:
            return True
        return int(self.height_map[row][column]) < int(self.height_map[row - 1][column])

    def _is_lower_than_bottom(self, row, column):
        if row == self.last_row:
            return True
        return int(self.height_map[row][column]) < int(self.height_map[row + 1][column])


class EndOfSearch(Exception):
    """Raised when a basin border is found"""


class BasinSizeFinder:
    def __init__(self, heigth_map: list[str]):
        self.height_map = heigth_map
        self.last_row = len(heigth_map) - 1
        self.last_column = len(heigth_map[0]) - 1

    def explore(self, starting_point: tuple, basin: set):
        row, column = starting_point

        for search_func in [
            self._look_left,
            self._look_right,
            self._look_above,
            self._look_down,
        ]:
            try:
                new_point = search_func(row, column)
                if new_point in basin:
                    continue

                basin.add(new_point)
                basin = self.explore(new_point, basin)
            except EndOfSearch:
                continue
        return basin

    def _look_left(self, row, column):
        if column == 0:
            raise EndOfSearch
        if (left := int(self.height_map[row][column - 1])) == 9:
            raise EndOfSearch
        if left > int(self.height_map[row][column]):
            return row, column - 1
        raise EndOfSearch

    def _look_right(self, row, column):
        if column == self.last_column:
            raise EndOfSearch
        if (right := int(self.height_map[row][column + 1])) == 9:
            raise EndOfSearch
        if right > int(self.height_map[row][column]):
            return row, column + 1
        raise EndOfSearch

    def _look_above(self, row, column):
        if row == 0:
            raise EndOfSearch
        if (above := int(self.height_map[row - 1][column])) == 9:
            raise EndOfSearch
        if above > int(self.height_map[row][column]):
            return row - 1, column
        raise EndOfSearch

    def _look_down(self, row, column):
        if row == self.last_row:
            raise EndOfSearch
        if (down := int(self.height_map[row + 1][column])) == 9:
            raise EndOfSearch
        if down > int(self.height_map[row][column]):
            return row + 1, column
        raise EndOfSearch


def part_2(heigth_map: list[str]):
    map_checker = MapChecker(heigth_map=heigth_map)
    low_points = map_checker.find_low_points()
    basin_sizes = []

    size_finder = BasinSizeFinder(heigth_map=heigth_map)
    for point in low_points:
        basin = size_finder.explore(point, basin={point})
        basin_sizes.append(len(basin))

    sorted_basin_sizes = sorted(basin_sizes, reverse=True)

    return prod(sorted_basin_sizes[:3])


if __name__ == "__main__":
    with open("day_09.txt", "r") as f:
        input_data = f.read().split("\n")

    answer_1 = part_1(input_data)
    print(answer_1)
    start = time()
    answer_2 = part_2(input_data)
    end = time()
    print(answer_2)
