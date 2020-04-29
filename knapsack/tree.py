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


@dataclass
class Node:
    item: Item
    value_sum: int
    rank: int
    capacity_remaining: int
    items: list

    @property
    def take_expectation(self,):
        exp = relaxed_linear_expecation(
            items=self.items[self.rank :],
            capacity=self.capacity_remaining,
            value=self.value_sum,
            weight=self.capacity_remaining,
        )
        return exp

    @property
    def pass_expectation(self,):

        exp = relaxed_linear_expecation(
            items=self.items[self.rank + 1 :],
            capacity=self.capacity_remaining,
            value=self.value_sum,
            weight=self.capacity_remaining,
        )
        return exp


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
    print(lines)
    firstLine = lines.pop(0).split()
    item_count = int(firstLine[0])
    capacity = int(firstLine[1])

    items = []

    for i in range(0, item_count):
        line = lines[i]
        parts = line.split()
        items.append(Item(i, int(parts[0]), int(parts[1])))

    items.sort(key=lambda x: x.density, reverse=True)

    rlc = relaxed_linear_expecation(items, capacity,)

    value_sum = 0
    capacity_remaining = capacity
    for rank, item in enumerate((items[0],)):
        n = Node(item, value_sum, rank, capacity_remaining, items)
        print(n.take_expectation)
        print(n.pass_expectation)

    return rlc


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
