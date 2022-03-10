from task1.count import list_element_counting


def test_list_element_counting():
    data = [
        "apple",
        "pear",
        "lemon",
        "orange",
        "pineapple",
        "tomato",
        "lettuce",
        "mango",
        "apple",
        "pineapple",
        "lemon",
        "pear",
        "pear",
    ]

    comparison_list = ['Apple', 'Pear', 'Lemon', 'Orange', 'Pineapple', 'Tomato', 'Mango', 'Banana']

    assert list_element_counting(data, comparison_list) == {'Apple': 2,
                                                            'Pear': 3,
                                                            'Lemon': 2,
                                                            'Orange': 1,
                                                            'Pineapple': 2,
                                                            'Tomato': 1,
                                                            'Mango': 1,
                                                            'Banana': 0, }