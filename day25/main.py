from typing import List
from collections import defaultdict
import functools

char_south = "v"
char_east = ">"
char_slot = "."


def split_chars(word: str) -> List[str]:
    result = []
    for ch in word:
        result.append(ch)
    return result


def move_east(grid: List[List[str]]) -> bool:
    is_moved = False
    l = len(grid[0])
    for row in grid:
        skip_next = False
        for col in range(1, l):
            if not skip_next and row[col - 1] == char_east and row[col] == char_slot:
                is_moved = True
                row[col - 1] = char_slot
                row[col] = char_east
                skip_next = True
            else:
                skip_next = False

        if not skip_next and row[col] == char_east and row[0] == char_slot:
            # print(f"[[c{col}]]")
            is_moved = True
            row[0] = char_east
            row[col] = char_slot

    return is_moved


def move_south(grid: List[List[str]]) -> bool:
    is_moved = False
    l = len(grid)
    for col in range(len(grid[0])):
        skip_next = False
        for row in range(1, l):
            if not skip_next and grid[row - 1][col] == char_south and grid[row][col] == char_slot:
                is_moved = True
                grid[row - 1][col] = char_slot
                grid[row][col] = char_south
                skip_next = True
            else:
                skip_next = False

        if not skip_next and grid[l - 1][col] == char_south and grid[0][col] == char_slot:
            is_moved = True
            # print(f"[[r{col}]]")
            grid[0][col] = char_south
            grid[l - 1][col] = char_slot

    return is_moved


if __name__ == "__main__":

    grid: List[List[str]] = list()
    with open("./data-1.txt", "r") as reader:
        lines = reader.read().splitlines()
        grid = [split_chars(line) for line in lines]

    rows = len(grid)
    cols = len(grid[0])

    def do_right_down(grid):
        move_east(grid)
        move_south(grid)

    do_right_down(grid)
    do_right_down(grid)
    do_right_down(grid)
    for line in grid:
        s = "".join(line)
        print(f"{s}")

    # print("------ START ------")
    # first = move_east(grid)
    # for line in grid:
    #     s = "".join(line)
    #     print(f"{s}")
    # print("-------------------")
    # second = move_south(grid)
    # for line in grid:
    #     s = "".join(line)
    #     print(f"{s}")
    # print("------- END -------")

    # count = 0
    # while move_east(grid) or move_south(grid):
    #     count += 1
    # print(f"Result: {count}")
    # for line in grid:
    #     s = "".join(line)
    #     print(f"{s}")
