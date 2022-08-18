from math import ceil
from random import randint

from models.cell import Cell


class Minefield:
    def __init__(self, difficult_mode='easy'):
        self.difficult_mode = difficult_mode
        self.cells = []
        self.game_over = False
        self.is_win = False
        self.first_step = True

        self.difficult_index = 0
        self.row_counter = 0
        self.column_counter = 0
        self.mine_counter = 0

        self.start_settings()
        self.start()

    def start_settings(self):
        dif_set = {
            'hard': (9, 9, 2),
            'medium': (6, 7, 1),
            'easy': (4, 4, 0)
        }
        self.row_counter, self.column_counter, self.difficult_index = dif_set[self.difficult_mode]

    def start(self):
        for i in range(self.row_counter):
            row_cells = []
            for j in range(self.column_counter):
                row_cells.append(Cell(i, j))

            self.cells.append(row_cells)

        if self.first_step:
            self.generate_mines()
            self.first_step = False

    def get_cell(self, row, column):
        if row < 0 or row >= self.row_counter or column < 0 or column >= self.column_counter:
            return None

        return self.cells[row][column]

    def generate_mines(self):
        if not self.first_step:
            return

        self.mine_counter = ceil(self.row_counter * self.column_counter / (6 - self.difficult_index))
        for i in range(self.mine_counter):
            while True:
                row = randint(0, self.row_counter - 1)
                column = randint(0, self.column_counter - 1)
                cell = self.get_cell(row, column)
                if cell.state != 'opened' and not cell.mined:
                    cell.mined = True
                    break

    def get_cell_neighbours(self, row, column):
        neighbours = []
        for r in range(row - 1, row + 2):
            neighbours.append(self.get_cell(r, column - 1))
            if r != row:
                neighbours.append(self.get_cell(r, column))

            neighbours.append(self.get_cell(r, column + 1))

        return filter(lambda n: n is not None, neighbours)

    def count_mines_around_cell(self, row, column):
        neighbours = self.get_cell_neighbours(row, column)
        return sum(1 for n in neighbours if n.mined)

    def open_cell(self, row, column):
        cell = self.cells[row][column]
        if not cell:
            return

        if cell.mined:
            self.game_over = True
            return

        cell.open()
        self.check_win()
        cell.counter = self.count_mines_around_cell(row, column)
        if cell.counter == 0:
            cell_neighbours = self.get_cell_neighbours(row, column)
            for n in cell_neighbours:
                if n.state == 'closed':
                    self.open_cell(n.row, n.column)

    def check_win(self):
        closed_cells = 0
        for i in range(self.row_counter):
            closed_cells += sum([1 for cell in self.cells[i] if cell.state == 'closed'])

        if self.mine_counter == closed_cells:
            self.game_over = True
            self.is_win = True
            return True

        return False

    def open_all_cells(self):
        for i in range(self.row_counter):
            for j in range(self.column_counter):
                self.cells[i][j].state = 'opened'

    def show(self):
        for i in range(self.row_counter):
            print([self.cells[i][j] for j in range(self.column_counter)])


if __name__ == '__main__':
    minefield = Minefield('easy')
    minefield.generate_mines()

    while not minefield.game_over:
        minefield.show()
        r, c = list(map(int, input('Enter row and column:').split()))
        minefield.open_cell(r, c)

        if minefield.is_win:
            print('WINNER')
            break
    else:
        print('LOSER')
