from collections import namedtuple, defaultdict
from dataclasses import dataclass


class Graph:
    start = 'start'
    end = 'end'

    def __init__(self, lines) -> None:
        self.graph = defaultdict(list)
        self.edges = self.normalise(lines=lines)
        self.paths = []

    def normalise(self, lines):
        return [point.split('-') for point in lines]

    def init_graph(self):
        for edge in self.edges:
            [a, b] = edge

            if a == self.start:
                self.graph[a].append(b)
            elif b == self.start:
                self.graph[b].append(a)
            else:
                self.graph[a].append(b)
                self.graph[b].append(a)
        del self.graph[self.end]
        return self.graph

    def is_valid_traverse(self, char: str, checked: dict) -> bool:
        # 1. big chars can be visited any number of times
        # 2. a single small char can be visited at most twice
        # 3. the remaining small chars can be visited at most once
        if char.islower():
            if char in checked:
                if checked['doubled']:
                    return checked[char] < 1
                return checked[char] < 2
            return True
        return True

    def find(self, node: str, traversed: set, current: list) -> None:
        if node == self.end:
            self.paths.append(current[:])
            return

        if not self.is_valid_traverse(node, traversed) or not self.graph[node]:
            return

        if node.islower():
            if node in traversed:
                traversed[node] += 1
                traversed['doubled'] = True
            else:
                traversed[node] = 1

        children = self.graph[node]
        for child in children:
            current.append(child)
            self.find(child, traversed.copy(), current)
            current.pop()

    def find_all_paths(self):
        traversed = {
            'doubled': False
        }
        self.find(self.start, traversed, [self.start])
        return self.paths


if __name__ == "__main__":
    with open("./data-2.txt", "r") as reader:
        lines = reader.read().splitlines()
        graph = Graph(lines)
        graph.init_graph()

        # all paths you find should visit small chars at most once, and can visit big chars any number of times
        #     start
        #     /   \
        # c--A-----b--d
        #     \   /
        #     end
        # ...
        # start -> [A, b] -> A -> [end, c, b] -> end
        # start -> [A, b] -> A -> c -> A -> end
        #
        # ...
        # Given these rules, there are 10 paths through this example:
        # start,A,b,A,c,A,end
        # start,A,b,A,end
        # start,A,b,end
        # start,A,c,A,b,A,end
        # start,A,c,A,b,end
        # start,A,c,A,end
        # start,A,end
        # start,b,A,c,A,end
        # start,b,A,end
        # start,b,end

        paths = graph.find_all_paths()
        print(len(paths))
