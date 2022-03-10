
from collections import Counter
from typing import List


def list_element_counting(input_list: List, comparison_list: List) -> dict:
    input_list = [i.capitalize() for i in input_list]
    transformed_list = []
    freq = Counter()
    freq.update({i: 0 for i in comparison_list})

    for food in input_list:
        if f"{food.capitalize()}" in comparison_list:
            transformed_list.append(food)

    count = Counter(transformed_list)

    freq.update(count)

    return freq
