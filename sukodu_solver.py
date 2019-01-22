class SudokuSolver:
    def __init__(self, puzzle):
        self.puzzle = puzzle

    def get_row(self, row_number):
        return self.puzzle[row_number]

    def get_column(self, column_number):
        return [row[column_number] for row in self.puzzle]

    def get_box(self, row_number, column_number):
        start_y = column_number // 3 * 3
        start_x = row_number // 3 * 3
        if start_x < 0: start_x = 0
        if start_y < 0: start_y = 0

        box = []
        for i in range(start_x, 3 + start_x):
            box.extend(self.puzzle[i][start_y:start_y+3])

        return box

    def get_possible_answers(self, row_number, column_number):
        if self.puzzle[row_number][column_number] != 0:
            return
        
        all_answers = range(1, 10)

        row = self.get_row(row_number)
        column = self.get_column(column_number)
        box = self.get_box(row_number, column_number)

        answered_values = set(row + column + box)

        possible_answers = [x for x in all_answers if x not in answered_values]
        return possible_answers

    def solve(self):
        unsolved = True

        while unsolved:
            unsolved = False

            for row in range(9):
                for column in range(9):
                    cell_value = self.puzzle[row][column]
                    if cell_value == 0:
                        unsolved = True
                        possible_answers = self.get_possible_answers(row, column)
                        
                        if len(possible_answers) == 0:
                            raise ValueError('A very specific bad thing happened.')

                        if len(possible_answers) == 1:
                            print(self.puzzle[row][column], possible_answers)
                            self.puzzle[row][column] = possible_answers[0]

        return self.puzzle

puzzle = [[5,3,0,0,7,0,0,0,0],
          [6,0,0,1,9,5,0,0,0],
          [0,9,8,0,0,0,0,6,0],
          [8,0,0,0,6,0,0,0,3],
          [4,0,0,8,0,3,0,0,1],
          [7,0,0,0,2,0,0,0,6],
          [0,6,0,0,0,0,2,8,0],
          [0,0,0,4,1,9,0,0,5],
          [0,0,0,0,8,0,0,7,9]]


solver = SudokuSolver(puzzle)

print(solver.solve())