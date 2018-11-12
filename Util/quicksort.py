import unittest


# sort a list of numbers
def quicksort(lst):
    if len(lst) <= 1:
        return lst

    pivot = lst[0]
    left, right = partition(lst[1:], pivot)
    return quicksort(left) + [pivot] + quicksort(right)


# lenght of lst is at least 1
def partition(lst, pivot):
    left = 0
    right = 0
    while right != len(lst):
        if lst[right] < pivot:
            lst[left], lst[right] = lst[right], lst[left]
            left += 1
        right += 1
    return lst[:left], lst[left:]


# the orginal lst remains unchanged after calling this method
def lomuto_quicksort_not_in_place(lst):
    if len(lst) <= 1:
        return lst
    pivot, lst1, lst2 = lst[-1], [], []
    for e in lst[:-1]:
        if e <= pivot:
            lst1.append(e)
        else:
            lst2.append(e)
    sorted_lst1 = lomuto_quicksort_not_in_place(lst1)
    sorted_lst2 = lomuto_quicksort_not_in_place(lst2)
    return sorted_lst1 + [pivot] + sorted_lst2


class TestQuicksort(unittest.TestCase):
    # return a list of tuples (lst_unsorted, expected)
    def data_provider(self):
        return [
            ([], []),
            ([1], [1]),
            ([1, 2], [1, 2]),
            ([2, 1], [1, 2]),
            ([3, 2, 1], [1, 2, 3]),
            ([1, 3, 2, 1, 2], [1, 1, 2, 2, 3]),
            ([6, 0, 8, 8, 8, 6, 7, 3, 3, 6], [0, 3, 3, 6, 6, 6, 7, 8, 8, 8]),
        ]

    # Date: 2015
    def test_quicksort(self):
        for lst_unsorted, expected in self.data_provider():
            self.assertEqual(quicksort(lst_unsorted), expected)

    # Date: Nov 11, 2018
    def test_lomuto_quicksort_not_in_place(self):
        for lst_unsorted, expected in self.data_provider():
            self.assertEqual(lomuto_quicksort_not_in_place(lst_unsorted), expected)


if __name__ == '__main__':
    unittest.main()
