import math

class Vector:
    def __init__(self, x=0, y=0) -> None:
        self.x = x
        self.y = y

    def __repr__(self) -> str:
        return f"'Vector({self.x!r}, {self.y!r})'"

    def __str__(self) -> str:
        # calls __repr__ as a fallback if __str__ is not implemented
        return f"Serialise: 'Vector({self.x!r}, {self.y!r})'"

    def __abs__(self):
        return math.hypot(self.x, self.y)

    def __bool__(self):
        return bool(abs(self))

    def __add__(self, other):
        x = self.x + other.x
        y = self.x + other.y
        return Vector(x, y)

    def __mul__(self, scalar):
        return Vector(self.x * scalar, self.y * scalar)


if __name__ == "__main__":
    v1 = Vector(2, 3)
    v2 = Vector(1, 9)
    v3 = v1 + v2

    print(f"1: {v3}")
    print(f"2: {str(v3)}")
    print(f"3: {repr(v3)}")