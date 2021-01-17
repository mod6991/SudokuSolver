"""
Sudoku library
Josué Clément (2021)
"""

class Sudoku:
    def __init__(self):
        self.gb = []
        self.possibilities = []
        for row_i in range(9):
            self.gb.append([])
            for col_i in range(9):
                self.gb[row_i].append(None)

    def get_row_values(self, row_i, avoid_cell=None):
        """
        Get row non-None values
        """
        s = set()
        for col_i in range(9):
            if self.gb[row_i][col_i]:
                if not avoid_cell or (row_i, col_i) != avoid_cell:
                    s.add(self.gb[row_i][col_i])
        return s

    def get_col_values(self, col_i, avoid_cell=None):
        """
        Get column non-None values
        """
        s = set()
        for row_i in range(9):
            if self.gb[row_i][col_i]:
                if not avoid_cell or (row_i, col_i) != avoid_cell:
                    s.add(self.gb[row_i][col_i])
        return s

    def get_square_values(self, row_i, col_i, avoid_cell=None):
        """
        Get square non-None values
        """
        row_start, row_stop = 0, 3
        col_start, col_stop = 0, 3

        if row_i in range(0, 3):
            row_start, row_stop = 0, 3
        elif row_i in range(3, 6):
            row_start, row_stop = 3, 6
        else:
            row_start, row_stop = 6, 9
        
        if col_i in range(0, 3):
            col_start, col_stop = 0, 3
        elif col_i in range(3, 6):
            col_start, col_stop = 3, 6
        else:
            col_start, col_stop = 6, 9
        
        s = set()

        for i in range(row_start, row_stop):
            for j in range(col_start, col_stop):
                if self.gb[i][j]:
                    if not avoid_cell or (i, j) != avoid_cell:
                        s.add(self.gb[i][j])

        return s

    def get_possibilities(self, row_i, col_i):
        an = set(range(1,10))
        s = set()
        s.update(self.get_row_values(row_i))
        s.update(self.get_col_values(col_i))
        s.update(self.get_square_values(row_i, col_i))
        return an.difference(s)

    def build_possibilities(self):
        """
        Build the possible values for each cell that doesn't
        containe a value
        """
        self.possibilities = []
        for row_i in range(9):
            self.possibilities.append([])
            for col_i in range(9):
                if self.gb[row_i][col_i]:
                    self.possibilities[row_i].append(None)
                else:
                    s = self.get_possibilities(row_i, col_i)
                    self.possibilities[row_i].append(s)

    def get_row_possibilities(self, row_i, avoid_cell=None):
        """
        Get the possible values of a given cell for its row.
        """
        s = set()
        for col_i in range(9):
            if self.possibilities[row_i][col_i]:
                if not avoid_cell or (row_i, col_i) != avoid_cell:
                    s.update(self.possibilities[row_i][col_i])
        return s

    def get_col_possibilities(self, col_i, avoid_cell=None):
        """
        Get the possible values of a given cell for its column.
        """
        s = set()
        for row_i in range(9):
            if self.possibilities[row_i][col_i]:
                if not avoid_cell or (row_i, col_i) != avoid_cell:
                    s.update(self.possibilities[row_i][col_i])
        return s

    def get_square_possibilities(self, row_i, col_i, avoid_cell=None):
        """
        Get the possible values of a given cell for its square.
        """
        row_start, row_stop = 0, 3
        col_start, col_stop = 0, 3

        if row_i in range(0, 3):
            row_start, row_stop = 0, 3
        elif row_i in range(3, 6):
            row_start, row_stop = 3, 6
        else:
            row_start, row_stop = 6, 9
        
        if col_i in range(0, 3):
            col_start, col_stop = 0, 3
        elif col_i in range(3, 6):
            col_start, col_stop = 3, 6
        else:
            col_start, col_stop = 6, 9
        
        s = set()

        for i in range(row_start, row_stop):
            for j in range(col_start, col_stop):
                if self.possibilities[i][j]:
                    if not avoid_cell or (i, j) != avoid_cell:
                        s.update(self.possibilities[i][j])

        return s

    def search_for_winners(self):
        """
        Search for unique possibilities
        """
        nb_winners = 0
        for row_i in range(9):
            for col_i in range(9):
                if not self.gb[row_i][col_i]:

                    if len(self.possibilities[row_i][col_i]) == 1:
                        print((row_i, col_i), '(len) ->', self.possibilities[row_i][col_i])
                        nb_winners += 1

                        for w in self.possibilities[row_i][col_i]:
                            self.gb[row_i][col_i] = w
                        continue

                    s = self.get_row_possibilities(row_i, (row_i, col_i))
                    for i in self.possibilities[row_i][col_i]:
                        if i not in s:
                            print((row_i, col_i), i, '(row) ->', self.possibilities[row_i][col_i])
                            nb_winners += 1
                            self.gb[row_i][col_i] = i
                            continue

                    s = self.get_col_possibilities(col_i, (row_i, col_i))
                    for i in self.possibilities[row_i][col_i]:
                        if i not in s:
                            print((row_i, col_i), i, '(col) ->', self.possibilities[row_i][col_i])
                            nb_winners += 1
                            self.gb[row_i][col_i] = i
                            continue
                            
                    s = self.get_square_possibilities(row_i, col_i, (row_i, col_i))
                    for i in self.possibilities[row_i][col_i]:
                        if i not in s:
                            print((row_i, col_i), i, '(sq) ->', self.possibilities[row_i][col_i])
                            nb_winners += 1
                            self.gb[row_i][col_i] = i
                            continue
        return nb_winners
