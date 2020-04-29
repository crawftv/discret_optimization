#!/usr/bin/python
# -*- coding: utf-8 -*-

from dataclasses import dataclass


@dataclass
class Item:
    index: int
    value: int
    weight: int
    taken: bool = False

    @property
    def density(self):
        return self.value / self.weight


def relaxed_linear_expecation(items, capacity, value=0, weight=0):
    """
    items: list of items
    weight: 
    value: 
    capacity: 
    """
    for item in items:
        if weight + item.weight <= capacity:
            value += item.value
            weight += item.weight
        elif weight + item.weight > capacity:
            try:
                fraction = item.weight / (capacity - weight)
                value += item.density * fraction
            except ZeroDivisionError:
                break
    return value


def solve_it(input_data):
    # Modify this code to run your optimization algorithm

    # parse the input
    lines = input_data.split("\n")
    firstLine = lines[0].split()
    item_count = int(firstLine[0])
    capacity = int(firstLine[1])

    items = []

    for i in range(1, item_count + 1):
        line = lines[i]
        parts = line.split()
        items.append(Item(i - 1, int(parts[0]), int(parts[1])))

    value = 0
    weight = 0
    sorted_items = sorted(items, key=lambda x: x.density, reverse=True)


    for index, item in enumerate(sorted_items):
        take = relaxed_linear_expecation(sorted_items[index:], capacity, value, weight)
        dont_take = relaxed_linear_expecation(
            sorted_items[index + 1 :], capacity, value, weight
        )
        print(index, value, weight, f"{item.weight}-{capacity}")
        print(f"rlc {take}")
        print(f"dont_take {dont_take}")

        if weight + item.weight <= capacity:
            item.taken = True
            value += item.value
            weight += item.weight

    # prepare the solution in the specified output format
    print(items)
    # output_data = str(value) + " " + str(0) + "\n"
    # output_data += " ".join(map(str, taken))
    # return output_data


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
