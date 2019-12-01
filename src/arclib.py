"""NUI Galway CT5132/CT5148 Programming and Tools for AI (James McDermott)

Common functions for Assignment 3
By writing my name below and submitting this file, I/we declare that
all additions to the provided skeleton file are my/our own work, and that
I/we have not seen any work on this assignment by another student/group.
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
    task_name = task_file[task_file.rindex('/'):-5]
    return json_data, task_name


class Task:
    """"
    Class for the problem task
    """

    # Private Methods

    # Constructor must have task name and input
    def __init__(self, task_name, task_input):
        print('init')
        self.__task_name = task_name
        self.__input = input
        self.__solution = self.__solve()

    def __solve(self):
        return self.__input

    # Public Methods
    def print_solution(self):
        print('solution for '+self.__task_name)
        print(self.__input,self.__solution)
