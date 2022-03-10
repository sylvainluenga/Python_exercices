from task3.recurrence import find_first_duplicate


def test_find_first_duplicate():
    data = [
        [2, 5, 1, 2, 3, 5, 1, 2, 4],  # Should return 2
        [2, 1, 1, 2, 3, 5, 1, 2, 4],  # Should return 1
        [2, 3, 4, 5],  # Should return None
        [2, 5, 5, 2, 3, 5, 1, 2, 4]  # Should return 5
    ]

    assert find_first_duplicate(data) == [2, 1, None, 5]