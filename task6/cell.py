class Cell:
    __slots__ = ('x', 'y')

    def get_neighbors(self):
        neighbors = []
        for x in range(self.x - 1, self.x + 2):
            for y in range(self.y - 1, self.y + 2):
                if (x, y) != (self.x, self.y):
                    neighbors.append(Cell(x, y))
        return neighbors

    def __init__(self, x: int, y: int):
        object.__setattr__(self, 'x', x)
        object.__setattr__(self, 'y', y)

    def __eq__(self, o: object) -> bool:
        return isinstance(o, Cell) and self.x == o.x and self.y == o.y

    def __hash__(self) -> int:
        return self.x * 34659649 + self.y * 785635867

    def __setattr__(self, *_):
        raise NotImplementedError

    def __delattr__(self, *_):
        raise NotImplementedError
