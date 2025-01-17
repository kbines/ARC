"""NUI Galway CT5132/CT5148 Programming and Tools for AI (James McDermott)

Common functions for Assignment 3
Student name(s): Keith Bines
Student ID(s): 19234297
"""
import json


# function to get json from file
def get_json(task_file):
    if task_file[-5:] != '.json':
        task_file = task_file + '.json'
    with open(task_file) as json_file:
        json_data = json.load(json_file)
    task_name = task_file[task_file.rindex('/') + 1:-5]
    return json_data, task_name


class Task:
    """"
    Class for the problem task
    """

    # Private Methods

    # Constructor must have task name and input
    def __init__(self, task_name, task_input):
        # create and set attributes
        self.__task_name = task_name
        self.__input = task_input
        self.__train = self.__input["train"]
        self.__test_input = self.__input["test"][0]["input"][0]
        self.__test_output = self.__input["test"][0]["output"]
        self.__solution = []
        self.__output = task_input

        # Call Solve
        self.__solve()

    def __solve(self):
        # use a dispatch table to easily extend for other solutions
        dt = {
            'feca6190': self.__solve_all_feca6190,
            'a64e4611': self.__solve_all_a64e4611,
            'ecdecbb3': self.__solve_all_ecdecbb3
        }
        dt[(self.__task_name)]()

        # Set the output to each training solution
        for training in range(0, len(self.__solution) - 1 ):
            self.__output["train"][training]["output"][0] = self.__solution[training]
        # Set last the test output to the test solution, the last grid
        self.__output["test"][0]["output"] = self.__solution[len(self.__solution) - 1]

    def __solve_all_feca6190(self):
        # Solve all training tasks
        for train_input in (range(0, len(self.__train))):
            print(self.__train[train_input]["input"][0])
            self.__solve_feca6190(self.__train[train_input]["input"][0])
        # solve test task
        self.__solve_feca6190(self.__input["test"][0]["input"][0])

    def __solve_all_a64e4611(self):
        # Solve all training tasks
        for train_input in (range(0, len(self.__train))):
            print(self.__train[train_input]["input"][0])
            self.__solve_a64e4611(self.__train[train_input]["input"][0])
        # solve test task
        self.__solve_a64e4611(self.__input["test"][0]["input"][0])

    def __solve_all_ecdecbb3(self):
        # Solve all training tasks
        for train_input in (range(0, len(self.__train))):
            print(self.__train[train_input]["input"][0])
            self.__solve_ecdecbb3(self.__train[train_input]["input"][0])
        # solve test task
        self.__solve_ecdecbb3(self.__input["test"][0]["input"][0])

    def __solve_feca6190(self, input):
        # see Readme for pseudo code
        # For this solution the grid size is a square of the number of coloured cells * the length of the input row
        coloured_cell_count = 0
        for cell in input:
            if cell > 0:
                coloured_cell_count += 1
        square = coloured_cell_count * len(input)
        solution_grid = self.__create_solution_grid(square, square)

        # For each coloured cell in the input
        start_cell = 0;
        solution_length = len(solution_grid)
        for colour in input:
            if colour > 0:
                # starting from the bottom row colour the cell at the same position as the test input cell
                # then move up 1 and right one until at the last column
                # Number of up movements is width of grid (square) - start position
                cell = start_cell
                for row in range(solution_length, start_cell, -1):
                    solution_grid[row-1][cell] = colour
                    cell += 1
            start_cell += 1
        self.__solution.append(solution_grid)

    def __solve_a64e4611(self, input):
        print('a64e4611')

    def __solve_ecdecbb3(self, input):
        print('ecdecbb3')

    # create the solution grid of size x,y set to all black (0)
    def __create_solution_grid(self, x, y):
        solution_grid = []
        for rows in range(y):
            row = [0] * x
            solution_grid.append(row)
        return solution_grid

    # Public Methods
    def print_solution(self):
        # todo for row in range(len(self.__solution)):["test"][0]["output"]
        for grid in self.__solution:
            for row in grid:
                print(' '.join(map(str, row)))
            print()

    def get_solution(self):
        return self.__output

    def test_input_output(self):
        if self.__output == self.__input:
            print("Success")
        else:
            print("Fail")

