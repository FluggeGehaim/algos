from time import perf_counter

from constat import (
    train_list_1000,
    train_list_751,
    train_list_500,
    train_list_321,
    train_list_99
    )

time_result: dict = {}


def get_min_item(data: list):
    min_item = data[0]
    min_item_index = 0
    for step in range(1, len(data)):
        if min_item > data[step]:
            min_item = data[step]
            min_item_index = step
    return min_item_index


def selection_sort(data: list):
    new_arr = []
    coppy_arr = data.copy()
    for step in range(len(coppy_arr)):
        smallest = get_min_item(coppy_arr)
        new_arr.append(coppy_arr.pop(smallest))
    return new_arr


def make_sort():
    data: list[list] = [train_list_1000,
                        train_list_751,
                        train_list_500,
                        train_list_321,
                        train_list_99]

    for test_name, incoming_data in enumerate(data):
        global time_result
        start_time = perf_counter()
        res = selection_sort(incoming_data)
        result_time = (perf_counter() - start_time)
        time_result.setdefault(test_name, result_time)
        print(res)
    return print("all tests completed")


make_sort()
for name, secs in time_result.items():
    print(f"{name}: {secs:.8f} сек")
