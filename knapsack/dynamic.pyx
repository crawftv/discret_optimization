#!/usr/bin/python
# -*- coding: utf-8 -*-

from dataclasses import dataclass
from math import floor
from functools import reduce


def solve_it(input_data):

    # @dataclass
    # class Item:
    #     index: int
    #     value: int
    #     weight: int
    #     taken: bool = False

    #     def __hash__(self):
    #         return self.index
    class Item:
        def __init__(self, index, value, weight, taken=False):
            self.index = index
            self.value = value
            self.weight = weight
            self.taken = taken

            def __hash__(self):
                return self.index

    lines = input_data.split("\n")
    firstLine = lines[0].split()
    item_count = int(firstLine[0])
    capacity = int(firstLine[1])
    items = []
    for i in range(1, item_count + 1):
        line = lines[i]
        parts = line.split()
        items.append(Item(i - 1, int(parts[0]), int(parts[1])))

    sorted_items = sorted(items, key=lambda x: x.weight)

    from functools import reduce

    old_list = [{"value": 0, "items": set()} for i in range(capacity + 1)]
    for item in sorted_items:
        new_list = old_list.copy()
        for i in range(item.weight, capacity + 1):
            trial_combo = set([item]).union(old_list[i - item.weight]["items"])
            trial_value = reduce(
                lambda x, y: x + y, [i.weight for i in list(trial_combo)]
            )
            if trial_value > old_list[i]["value"]:
                new_list[i]["items"] = trial_combo
                new_list[i]["value"] = trial_value

    for i in new_list[capacity]["items"]:
        i.taken = True

    # prepare the solution in t
    # he specified output format

    taken = [int(i.taken) for i in items]
    value = new_list[capacity]["value"]
    output_data = str(value) + " " + str(0) + "\n"
    output_data += " ".join(map(str, taken))
    return output_data
