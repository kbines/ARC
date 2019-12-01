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
        self.__test_input = self.__input["test"][0]["input"][0]
        self.__test_output = self.__input["test"][0]["output"]
        self.__solution = []

        # Call Solve
        self.__solve()


    def __solve(self):
        # use a dispatch table to easily extend for other solutions
        dt = {
            ('feca6190'): self.__solve_feca6190,
            ('a64e4611'): self.__solve_a64e4611,
            ('66e6c45b'): self.__solve_66e6c45b
        }
        dt[(self.__task_name)]()
        return self.__solution

    # create the solution grid of size x,y set to all black (0)
    def __create_solution_grid(self, x, y):
        for rows in range(y):
            row = [0] * x
            self.__solution.append(row)

    def __solve_feca6190(self):
        # see Readme for psuedo code
        # For this solution the grid size is a square of the number of coloured cells * the length of the input row
        coloured_cell_count = 0
        for cell in self.__test_input:
            if cell > 0:
                coloured_cell_count += 1
        square = coloured_cell_count * len(self.__test_input)
        self.__create_solution_grid(square, square)

        # For each coloured cell in the input
        start_cell = 0;
        solution_length = len(self.__solution)
        for colour in self.__test_input:
            if colour > 0:
                # starting from the bottom row colour the cell at the same position as the test input cell
                # then move up 1 and right one until at the last column
                # Number of up movements is width of grid (square) - start position
                cell = start_cell
                for row in range(solution_length, start_cell, -1):
                    self.__solution[row-1][cell] = colour
                    cell += 1
            start_cell += 1

    def __solve_a64e4611(self):
        print('a64e4611')

    def __solve_66e6c45b(self):
        print('66e6c45b')

    # Public Methods
    def print_solution(self):
        # todo for row in range(len(self.__solution)):["test"][0]["output"]
        for row in self.__solution:
            print(' '.join(map(str,row)))
        print()