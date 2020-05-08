#!/usr/bin/python
# -*- coding: utf-8 -*-

from dataclasses import dataclass
from math import floor
from functools import reduce


@dataclass
class Item:
    index: int
    value: int
    weight: int
    taken: bool = False

    @property
    def density(self):
        return self.value / self.weight


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

    sorted_items = sorted(items, key=lambda x: x.weight)

    item_dict = {
        item.weight: {"value": item.value, "items": item.weight}
        for item in sorted_items
    }

    capacity_dict = {0: {"value": 0, "items": set()}}
    for ww in range(1, capacity + 1):
        # simple searches
        item_lookup = item_dict.get(ww, {"value": 0})
        previous_value = capacity_dict.get(ww - 1, {"value": 0})
        if item_lookup["value"] >= previous_value["value"]:
            vv = {"value": item_lookup["value"], "items": {ww}}
        else:
            vv = previous_value

        capacity_dict[ww] = vv

        # lookup combinations
        for i in range(1, floor((ww + 1) / 2)):
            # print(f"{i}:{capacity_dict[i]} --- {ww-i}:{capacity_dict[ww-i]}")
            uu = capacity_dict[i]["items"].union(capacity_dict[ww - i]["items"])
            new_sum = 0
            for i in list(uu):
                id = item_dict.get(i, {"weight": 0, "value": 0})
                new_sum += id["value"]
            if new_sum > capacity_dict[ww]["value"]:
                capacity_dict[ww] = {"value": new_sum, "items": uu}

    # prepare the solution in the specified output format
    final_items = {item.weight: item for item in items}
    for i in capacity_dict[capacity]["items"]:
        final_items[i].taken = True
    taken = [int(i.taken) for i in items]
    value = capacity_dict[capacity]["value"]
    output_data = str(value) + " " + str(0) + "\n"
    output_data += " ".join(map(str, taken))
    return output_data


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
