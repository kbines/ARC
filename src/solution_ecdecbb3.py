"""NUI Galway CT5148 Programming and Tools for AI (James McDermott)
Task ecdecbb3 for Assignment 3
Student name(s): Keith Bines
Student ID(s): 19234297
"""
from sys import argv
import arclib

def solve(grid):
    print('in solve')
    task = arclib.Task(taskname, grid)
    task.print_solution()
    json_solution = task.get_solution()
    # task.test_input_output()

def main():
    print('in main')
    global taskname
    json, taskname = arclib.get_json(argv[1])
    solve(json)

if __name__ == "__main__":
    main()
