from time import perf_counter

import constat

time_result = {}


def bubble_sort(data: list):
    iterations = len(data) - 1
    for first_step in range(iterations):
        for second_step in range(iterations - first_step):
            if data[second_step] > data[second_step + 1]:
                data[second_step], data[second_step + 1] = data[second_step + 1], data[second_step]
    return data


def make_sort():
    data: list[list] = [constat.train_list_1000,
                        constat.train_list_751,
                        constat.train_list_500,
                        constat.train_list_321,
                        constat.train_list_99]

    for test_name, incoming_data in enumerate(data):
        global time_result
        start_time = perf_counter()
        res = bubble_sort(incoming_data)
        result_time = (perf_counter() - start_time)
        time_result.setdefault(test_name, result_time)
        print(res)
    return print("all tests completed")


make_sort()
for name, secs in time_result.items():
    print(f"{name}: {secs:.8f} сек")
