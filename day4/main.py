from typing import List
from collections import namedtuple
from dataclasses import dataclass


def print_table(table: List[List[int]]) -> None:
    for row in table:
        print(row)


def build_marked(count: int, dimension: int) -> List[List[List[int]]]:
    result = []
    for _ in range(0, count):
        matr = []
        for _ in range(0, dimension):
            row = [0 for _ in range(0, dimension)]
            matr.append(row)
        result.append(matr)
    return result


def mark_and_check(
    board: List[List[int]],
    marked: List[List[int]],
    number: int
) -> List[int] | bool:
    # mark visited cells/numbers
    for i in range(0, len(board)):
        for j in range(0, len(board[0])):
            if board[i][j] == number:
                marked[i][j] = 1

    # check if bingo
    for k in range(0, len(marked)):
        # check row
        is_full_row = True
        for l in range(0, len(marked[0])):
            if not marked[k][l]:
                is_full_row = False
        if is_full_row:
            return list(board[k])

        # check col
        is_full_col = True
        column_numbers = []
        for m in range(0, len(marked[0])):
            column_numbers.append(board[m][k])
            if not marked[m][k]:
                is_full_col = False
        if is_full_col:
            return column_numbers

    return False


def find_unmarked_sum(board: List[List[int]], marked: List[List[int]]) -> int:
    sum = 0
    for i in range(0, len(board)):
        for j in range(0, len(board[0])):
            if not marked[i][j]:
                sum += board[i][j]
    return sum


if __name__ == "__main__":
    randoms = []
    boards = []
    with open("./data-2.txt", "r") as reader:
        lines = reader.read().splitlines()
        randoms = [int(x) for x in lines[0].split(',')]

        board = []
        for line in lines[2:]:
            if not line:
                boards.append(board)
                board = []
            else:
                board.append([int(x) for x in line.split()])
        boards.append(board)

    boards_num = len(boards)
    dim = 5
    marked = build_marked(boards_num, dim)

    check_board_win = [0 for _ in range(0, boards_num)]
    for number in randoms:
        is_finished = False

        for i in range(0, boards_num):
            has_crossed = mark_and_check(boards[i], marked[i], number)

            if has_crossed:
                check_board_win[i] = 1
                print(check_board_win)

                if all(check_board_win):
                    sum = find_unmarked_sum(boards[i], marked[i])
                    print(i, sum, number, has_crossed)
                    print(f'Result: {(sum * number)}')
                    is_finished = True

                    # print_table(boards[i])
                    # for board in boards:
                    #     print_table(board)
                    # print_table(marked[i])
                    # for m in marked:
                    #     print_table(m)
                    break

        if is_finished:
            break
