#!/usr/bin/python3

import inspect
import os

#Whether to use a sample file or not.
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
    return os.path.abspath(f"{os.path.dirname(_top_level_caller())}/inputs/Day{get_day()}{'.s' if SAMPLE else ''}txt")


def input_file():
    """get a reference straight to the input file"""
    return open(filepath(), "r", encoding='UTF-8')


def input_string():
    """read input into a string"""
    return open(filepath(), "r", encoding='UTF-8').read().strip()


def input_int_list():
    """parse input into a list of ints"""
    with open(filepath(), "r", encoding='UTF-8') as file:
        return [int(line.rstrip()) for line in file]


def input_string_list():
    """parse input into a list of strings"""
    with open(filepath(), "r", encoding='UTF-8') as file:
        return [line.rstrip() for line in file]


def input_block_list():
    """input split by paragraph i.e. two newlines"""
    with open(filepath(), "r", encoding='UTF-8') as file:
        return file.read().strip().split("\n\n")


def input_tab_list():
    """input split by tab i.e. \\t"""
    with open(filepath(), "r", encoding='UTF-8') as file:
        return [line.rstrip('\n').split('\t') for line in file]

def filter_empty(li):
    """remove empty entries (e.g. when splitting a string)"""
    return list(filter(None, li))
