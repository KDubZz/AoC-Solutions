#!/usr/bin/python3

import inspect
import os

"""Whether to use a test file"""
SAMPLE = False


def _top_level_caller():
    """get the filename of the original script that called this up"""
    return inspect.stack()[-1].filename


def get_day():
    """
    get the day of the python script calling this function
    NB: no validation for filename, it is assumed to be DayXX.py
    """
    return os.path.basename(_top_level_caller())[3:5]


def filepath():
    """get the filepath of the input"""
    return os.path.abspath(
        f"{os.path.dirname(_top_level_caller())}/{'Day'}{get_day()}{'.s' if SAMPLE else ''}txt"
    )


def input():
    """get a reference straight to the input file"""
    return open(filepath(), "r")


def input_string():
    """read input into a string"""
    return open(filepath(), "r").read().strip()


def input_int_list():
    """parse input into a list of ints"""
    with open(filepath(), "r") as file:
        return [int(line.rstrip()) for line in file]


def input_string_list():
    """parse input into a list of strings"""
    with open(filepath(), "r") as file:
        return [line.rstrip() for line in file]


def input_block_list():
    """input split by paragraph i.e. two newlines"""
    with open(filepath(), "r") as file:
        return file.read().strip().split("\n\n")


def filter_empty(li):
    """remove empty entries (e.g. when splitting a string)"""
    return list(filter(None, li))


def sum_list(li):
    """converts all values in list to integer and finds sum"""
    y = [eval(i) for i in li]
    c = 0
    for b in range(len(y)):
        c += y[b]
    return c


