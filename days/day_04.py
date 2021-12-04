_ROWS_IN_BOARD = 5
_NUMBERS_IN_ROW = 5


class BingoNotFound(Exception):
    """No Bingo"""


def part_1(data: list[str]):

    drawn_numbers = [number for number in data[0].split(",")]
    board_numbers_str = "," + _parse_bingo_boards(str_data[1:]) + ","

    drawn_number, board_idx = 0, 0
    bingo_idx_list = []
    for drawn_number in drawn_numbers:
        board_numbers_str = board_numbers_str.replace(f",{drawn_number},", ",🎅,")

        board_numbers_list = board_numbers_str.strip(",").split(",")
        try:
            bingo_idx_list = find_bingo(board_numbers_list, bingo_idx_list)
            break
        except BingoNotFound:
            continue

    board_idx = bingo_idx_list[0]
    board_numbers_list = board_numbers_str.strip(",").split(",")
    board_start_idx = board_idx * 25
    board = board_numbers_list[board_start_idx: board_start_idx + 25]
    remaining_sum = sum([int(number) for number in board if number != "🎅"])
    return remaining_sum * int(drawn_number)


def find_bingo(board_numbers_list, bingo_idx_list):

    new_bingos = []
    for idx in range(0, len(board_numbers_list), 5):
        if idx // 25 in bingo_idx_list + new_bingos:
            continue
        if board_numbers_list[idx: idx + 5] == ["🎅"] * 5:
            new_bingos.append(idx // 25)
            continue

    for idx in range(0, len(board_numbers_list), 25):
        if idx // 25 in bingo_idx_list + new_bingos:
            continue
        for offset in range(5):
            start_idx = idx + offset
            if board_numbers_list[start_idx: start_idx + 25: 5] == ["🎅"] * 5:
                new_bingos.append(idx // 25)
                break
    if not new_bingos:
        raise BingoNotFound

    bingo_idx_list += new_bingos
    return bingo_idx_list


def part_2(data: list[str]):

    drawn_numbers = [number for number in data[0].split(",")]
    board_numbers_str = "," + _parse_bingo_boards(str_data[1:]) + ","

    drawn_number, board_idx = 0, 0
    bingo_idx_list = []
    for idx, drawn_number in enumerate(drawn_numbers):
        board_numbers_str = board_numbers_str.replace(f",{drawn_number},", ",🎅,")

        board_numbers_list = board_numbers_str.strip(",").split(",")
        try:
            bingo_idx_list = find_bingo(board_numbers_list, bingo_idx_list)
        except BingoNotFound:
            continue
        if len(bingo_idx_list) == len(board_numbers_list) // 25:
            break

    last_board_idx = bingo_idx_list[-1]
    board_numbers_list = board_numbers_str.strip(",").split(",")
    board_start_idx = last_board_idx * 25
    board = board_numbers_list[board_start_idx: board_start_idx + 25]
    remaining_sum = sum([int(number) for number in board if number != "🎅"])
    return remaining_sum * int(drawn_number)


def _parse_bingo_boards(board_str: str):
    _NUMBERS_IN_BOARD = 25

    board_row_list = [board_row.strip() for board_row in board_str if board_row]
    board_numbers = [number for board in board_row_list for number in board.split(" ") if number]
    return ",".join(board_numbers)


if __name__ == "__main__":
    with open("day_04.txt", "r") as f:
        str_data = f.read().splitlines()

    answer_1 = part_1(str_data)
    print(answer_1)

    answer_2 = part_2(str_data)
    print(answer_2)
