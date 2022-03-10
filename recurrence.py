from typing import List


def first_uplicate(input_list: List) -> int or None:
    set_ = set()
    for item in input_list:
        if item in set_:
            return item
        set_.add(item)
    return None


def find_first_duplicate(lists: List) -> List:
    duplicates = []

    for l in lists:
        duplicates.append(first_uplicate(l))

    return duplicates