class Cell:
    def __init__(self, row, column):
        self.row = row
        self.column = column
        self.state = 'closed'
        self.mined = False
        self.counter = 0

    def open(self):
        self.state = 'opened'

    def __repr__(self):
        # return f"{'*' if self.state == 'closed' else self.counter}"
        return f"{'1' if self.mined else '0'}"
