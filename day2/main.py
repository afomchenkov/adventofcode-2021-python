from typing import List
from collections import namedtuple
from dataclasses import dataclass
import functools

Step = namedtuple('Step', 'name move')


def parse_line(line: str) -> Step:
    return Step(*line.split())

# first step
# - forward X increases the horizontal position by X units.
# - down X increases the depth by X units.
# - up X decreases the depth by X units.
# ---
# second step
# - down X increases your aim by X units.
# - up X decreases your aim by X units.
# - forward X does two things:
#   - It increases your horizontal position by X units.
#   - It increases your depth by your aim multiplied by X.


@dataclass
class Mover:
    row = 0
    col = 0
    aim = 0
    steps = list()

    def register(self, parsed_steps: List[Step]) -> None:
        self.steps = parsed_steps

    def run(self) -> None:
        for step in self.steps:
            move = int(step.move)
            print(step, move)

            match step.name:
                case 'forward':
                    self.col += move
                    self.row += self.aim * move
                case 'down':
                    # self.row += move
                    self.aim += move
                case 'up':
                    # self.row -= move
                    self.aim -= move

    def print(self) -> None:
        print(f'Depth:{self.row}, Horiz:{self.col}, Mult:{self.row * self.col}')


if __name__ == "__main__":
    mover = Mover()
    with open("./data-2.txt", "r") as reader:
        lines = reader.read().splitlines()
        mover.register([parse_line(line) for line in lines])

    mover.run()
    mover.print()
