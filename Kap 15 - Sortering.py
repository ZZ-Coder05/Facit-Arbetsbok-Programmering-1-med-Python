from random import randrange
import time

def quick_sort(sequence):
    length = len(sequence)

    if length <= 1:
        return sequence
    else:
        pivot = sequence.pop()

    items_greater = []
    items_smaller = []

    for item in sequence:
        if item > pivot:
            items_greater.append(item)
        else:
            items_smaller.append(item)

    return quick_sort(items_smaller) + [pivot] + quick_sort(items_greater)

def insertion_sort():
    pass

def bubble(sequence):
    indexing_length = len(sequence) - 1
    is_sorted = False
    while not is_sorted:
        is_sorted = True
        for i in range(indexing_length):
            if sequence[i] > sequence[i + 1]:
                is_sorted = False
                sequence[i], sequence[i + 1] = sequence[i + 1], sequence[i]
    return sequence


def sort_test():
    test_list = [randrange(1, 1001) for i in range(1000)]
    st = time.process_time()
    bubble(test_list)
    et = time.process_time()
    print("Time taken in seconds: {:<20f}".format(et - st))


def uppg1(sequence):
    """
    loop through n-1 elements
        no swap yet
        loop through
    """

if __name__ == '__main__':
    sort_test()