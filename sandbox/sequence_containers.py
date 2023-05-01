from array import array
from collections import abc
import os
import keyword

# keyword.softkwlist

"""
    Every Python object in memory has a header with metadata.
    For example float type has a value field and two metadata fields:
        - ob_refcnt: object references count
        - ob_type: a pointer to the object's type
        - ob_fval: a C double holding the value of the float


    > mutable sequences: list, bytearray, array.array, collections.deque
    > immutable sequences: tuple, str, bytes
"""


class Object(object):
    def __init__(self) -> None:
        pass

# list comprehension
def build_codes_list():
    symbols = '$^%#'
    codes = [ord(symbol) for symbol in symbols]
    beyond_ascii_1 = [ord(s) for s in symbols if ord(s) > 127]
    beyond_ascii_2 = list(filter(lambda c: c > 127, map(ord, symbols)))
    return (codes, (beyond_ascii_1, beyond_ascii_2))

def cartesian_mult():
    colors = ['black', 'white']
    sizes = ['S', 'M', 'L']
    tshirts = [(color, size) for color in colors for size in sizes]
    return tshirts

# generator expression
def init_from_generator_expression():
    """
        Generator expression yields items one by one, does not create instance in memory
    """
    symbols = '^&*@$)*'
    result1 = tuple(ord(symbol) for symbol in symbols) # as a single argument
    result2 = array('i', (ord(symbol) for symbol in symbols))
    return (result1, result2)

def check_if_fixed(o):
    try:
        hash(o)
    except TypeError:
        return False
    return True


if __name__ == "__main__":
    # flat sequence stores the value of its contents in its own memory space
    flat_sequence = array('d', [9.46, 2.08, 4.29])
    obj1 = Object()
    print(type(flat_sequence))
    print(type(obj1) == Object)
    print(isinstance(obj1, object))

    print(issubclass(tuple, abc.Sequence))
    print(issubclass(tuple, abc.MutableSequence))

    # unpacking
    coordinates = (33.9425, -118.408056)
    latitude, longitude = coordinates
    # a, b = b, a
    t = (20, 8)
    quotient, remainder = divmod(*t)

    _, fielname = os.path.split('/home/Documents/sandbox/test.txt')

    # take excess items
    a, b, *rest = range(5)
    a, *body, c, d = range(5)

    def fun(a, b, c, d, *rest):
        return a, b, c, d, rest
    result1 = fun(*[1, 2], 3, *range(4, 7)) # (1, 2, 3, 4, (5, 6))


    tf = (10, 'alpha', (1, 2))
    tm = (10, 'alpha', [1, 2])
    print(f"tf: {check_if_fixed(tf)}")
    print(f"tm: {check_if_fixed(tm)}")
