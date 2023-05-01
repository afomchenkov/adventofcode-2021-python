from typing import List
from collections import namedtuple
from dataclasses import dataclass

"""
    [[from, to], [from, to]]
    x1, y1 -> x2, y2
    from [x, y] -> to [x, y]
"""


def parse_coordinates(s: str) -> List[int]:
    return [int(c) for c in s.split(',')]


def build_grid(x: int, y: int) -> List[List[int | str]]:
    return [['.' for _ in range(0, y)] for _ in range(0, x)]


def is_vertical_move(move: List[List[int]]) -> bool:
    begin, end = move
    return begin[0] == end[0]


def is_horizontal_move(move: List[List[int]]) -> bool:
    begin, end = move
    return begin[1] == end[1]


def mark_cell(grid: List[List[int | str]], y: int, x: int) -> None:
    if grid[x][y] == '.':
        grid[x][y] = 1
    else:
        grid[x][y] += 1


def register_move(grid: List[List[int | str]], move: List[int]) -> None:
    begin, end = move

    x1, y1 = begin
    x2, y2 = end

    # vertcal move
    if is_vertical_move(move):
        begin = min(y1, y2)
        end = max(y1, y2)
        for c in range(begin, end + 1):
            mark_cell(grid, x1, c)
        return None

    # horizontal move
    if is_horizontal_move(move):
        begin = min(x1, x2)
        end = max(x1, x2)
        for c in range(begin, end + 1):
            mark_cell(grid, c, y1)
        return None

    # diagonal only if:
    #  - from right top to left bottom (x++, y++)
    #  - from right bottom to left top (x++, y--)
    #  - from left bottom to right top (x--, y--)
    #  - from left top to right bottom (x--, y++)

    if y1 < y2:
        # move from top to bottom
        if x1 < x2:
            # from left top to right bottom
            for col in range(y1, y2 + 1):
                mark_cell(grid, x1, col)
                x1 = x1 + 1
        else:
            # from right top to left bottom
            for col in range(y1, y2 + 1):
                mark_cell(grid, x1, col)
                x1 = x1 - 1
    else:
        # move from bottom to top
        if x1 < x2:
            # from left bottom to right top
            for col in range(y1, y2 - 1, -1):
                mark_cell(grid, x1, col)
                x1 = x1 + 1
        else:
            # from right bottom to left top
            for col in range(y1, y2 - 1, -1):
                mark_cell(grid, x1, col)
                x1 = x1 - 1


def count_overlaps(grid: List[List[int | str]]) -> int:
    count = 0
    for row in grid:
        for cell in row:
            if cell != '.' and cell >= 2:
                count += 1
    return count


if __name__ == "__main__":
    moves = []
    with open("./data-2.txt", "r") as reader:
        lines = reader.read().splitlines()
        for line in lines:
            moves.append([parse_coordinates(s)
                         for s in line.split() if s != '->'])

    rows = cols = 1000
    grid = build_grid(rows, cols)

    for move in moves:
        register_move(grid, move)
    # for row in grid:
    #     print(' '.join(map(lambda a: str(a), row)))
    print(count_overlaps(grid))
