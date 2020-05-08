#!/usr/bin/python
# -*- coding: utf-8 -*-

from dataclasses import dataclass
from math import floor
from functools import reduce


def solve_it(input_data):
    from dynamic import solve_it as d_solve_it

    output = d_solve_it(input_data)
    return output


if __name__ == "__main__":
    import sys

    if len(sys.argv) > 1:
        file_location = sys.argv[1].strip()
        with open(file_location, "r") as input_data_file:
            input_data = input_data_file.read()
        print(solve_it(input_data))
    else:
        print(
            "This test requires an input file.  Please select one from the data directory. (i.e. python solver.py ./data/ks_4_0)"
        )
