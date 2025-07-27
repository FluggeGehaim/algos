from time import perf_counter
from random import randint

from constat import (
    train_list_1000,
    train_list_751,
    train_list_500,
    train_list_321,
    train_list_99
    )

time_result: dict = {}


def binary_search(data: list[int], need_to_find: int) -> int | None:
    low, high = 0, len(data) - 1
    while low <= high:
        midd = (low + high) // 2
        guess = data[midd]
        if guess == need_to_find:
            return guess
        elif need_to_find > guess:
            low = midd + 1
        else:
            high = midd - 1

    return None


def make_calculation():
    data: list[list] = [train_list_1000,
                        train_list_751,
                        train_list_500,
                        train_list_321,
                        train_list_99]

    for test_name, incoming_data in enumerate(data):
        global time_result
        incoming_data = sorted(incoming_data)
        need_to_find: int = randint(min(incoming_data), len(incoming_data) - 1)
        start_time = perf_counter()

        binary_search(incoming_data, need_to_find)
        result_time = (perf_counter() - start_time)
        time_result.setdefault(test_name, result_time)

    return print("all tests completed")


make_calculation()

for name, secs in time_result.items():
    print(f"{name}: {secs:.8f} сек")