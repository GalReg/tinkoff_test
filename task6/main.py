import os
import sys
import time
from field import Field


class Main:
    @staticmethod
    def __test_unicode(c: str) -> bool:
        """Проверяет возможность вывода символа 'c' в консоль"""
        try:
            c.encode(sys.stdout.encoding)
            return True
        except UnicodeEncodeError:
            return False

    @staticmethod
    def __read_field():
        """Считывает поле из консоли"""
        rows = []
        row = input()
        while row:
            rows.append(row)
            row = input()
        return '\n'.join(rows)

    @staticmethod
    def __input_prompt() -> str:
        print("Conway's Game of Life")
        print('1) Random initial field')
        print('2) Manual input')

        choice = input()
        while not '1' <= choice <= '2':
            print('Invalid input')
            choice = input()

        if choice == '1':
            return ''

        print('0 - empty, 1 - cell, empty string to stop input')
        return Main.__read_field()

    @staticmethod
    def main():
        clear_command = 'cls' if os.name == 'nt' else 'clear'

        initial_state = Main.__input_prompt()
        cell_symbol = '█' if Main.__test_unicode('█') else '@'
        b = Field(initial_state, cell_symbol)

        for _ in range(100):
            os.system(clear_command)
            b.next_step()
            print(b.to_string())
            time.sleep(0.35)


if __name__ == '__main__':
    Main.main()
