from typing import List


def insertion_sort(numbers):
    len_numbers = len(numbers)
    for i in range(1, len_numbers):
        tmp = numbers[i]
        j = i - 1
        while j >= 0 and numbers[j] > tmp:
            numbers[j + 1] = numbers[j]
            j -= 1


if __name__ == "__main__":
    import random
    numbers = [random.randint(0, 1000) for i in range(10)]
    insertion_sort(numbers)
    print(numbers)