from typing import List
from collections import namedtuple
from dataclasses import dataclass

if __name__ == "__main__":
    with open("./data-2.txt", "r") as reader:
        lines = reader.read().splitlines()
        values = [int(val) for val in lines[0].split(',')]

        # Initial state: 3,4,3,1,2                - [0, 1, 1, 2, 1, 0, 0, 0, 0] shift
        # After  1 day:  2,3,2,0,1                - [1, 1, 2, 1, 0, 0, 0, 0, 0] shift
        # After  2 days: 1,2,1,6,0,8              - [1, 2, 1, 0, 0, 0, 1, 0, 1] shift & add +1 day6,8
        # After  3 days: 0,1,0,5,6,7,8            - [2, 1, 0, 0, 0, 1, 1, 1, 1] shift & add +1 day6,8
        # After  4 days: 6,0,6,4,5,6,7,8,8        - [1, 0, 0, 0, 1, 1, 3, 1, 2] shift & add +2 day6,8
        # After  5 days: 5,6,5,3,4,5,6,7,7,8      - ...
        # After  6 days: 4,5,4,2,3,4,5,6,6,7      - ...
        # After  7 days: 3,4,3,1,2,3,4,5,5,6      

        reset_to = 6
        default_new_timer = 8
        days_cycle = 256

        born_list = [0] * 9 # index - day, value - count of fishes
        days_count = 0

        for value in values:
            born_list[value] += 1

        while days_count < days_cycle:
            days_count += 1
            new_born_list = [0] * 9
            count_of_borns = 0
            for idx, val in enumerate(born_list):
                if idx == 0:
                    count_of_borns = val
                else:
                    new_born_list[idx - 1] = val
            new_born_list[default_new_timer] = count_of_borns
            new_born_list[reset_to] += count_of_borns
            born_list = new_born_list

    print(sum(born_list))
