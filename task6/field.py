from collections import defaultdict
from cell import Cell
import random


class Field:
    @staticmethod
    def __generate_random_field() -> str:
        n_rows = random.randrange(8, 12)
        n_columns = random.randrange(8, 12)
        rows = (''.join(random.choices('01', k=n_columns)) for _ in range(n_rows))
        return '\n'.join(rows)

    def __init__(self, initial_state: str, cell_symbol: str):
        if not initial_state.strip():
            initial_state = Field.__generate_random_field()

        self._cell_symbol = cell_symbol * 2 #
        self._field = set()
        for row, line in enumerate(initial_state.split("\n")):
            line = ''.join(filter(lambda c: c == '0' or c == '1', line))
            for col, elem in enumerate(line):
                if elem == '1':
                    self._field.add(Cell(col, row))

    def next_step(self):
        field = set()
        for cell, count in self.__count_neighbors().items():
            if count == 3 or (cell in self._field and count == 2):
                field.add(cell)
        self._field = field

    def to_string(self):
        if not self._field:
            return "~~~~\n~~~~"
        padding_size = 1
        field_str = ''
        x_min, x_max, y_min, y_max = self.__find_range()
        for y in range(y_min - padding_size, y_max + 1 + padding_size):
            for x in range(x_min - padding_size, x_max + 1 + padding_size):
                field_str += self._cell_symbol if Cell(x, y) in self._field else '~~'
            field_str += '\n'
        return field_str.strip()

    def __count_neighbors(self):
        neighbor_counts = defaultdict(int)
        for cell in self._field:
            for neighbor in cell.get_neighbors():
                neighbor_counts[neighbor] += 1
        return neighbor_counts

    def __find_range(self):
        x_min = y_min = float('inf')
        x_max = y_max = -float('inf')

        for cell in self._field:
            if cell.x > x_max:
                x_max = cell.x
            if cell.x < x_min:
                x_min = cell.x

            if cell.y > y_max:
                y_max = cell.y
            if cell.y < y_min:
                y_min = cell.y

        return x_min, x_max, y_min, y_max
