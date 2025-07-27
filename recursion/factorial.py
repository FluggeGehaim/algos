from utils import get_time

from constat import (
    num_5,
    num_7,
    num_12,
    num_23,
    num_41
)

time_result = {}


@get_time
def get_factorial(num: int):
    if num <= 1:
        return 1
    return num * get_factorial(num - 1)[0]


def make_test():
    data: list[list] = [
        num_5,
        num_7,
        num_12,
        num_23,
        num_41
    ]

    for test_name, incoming_data in enumerate(data):
        global time_result
        result, result_time = get_factorial(incoming_data)
        time_result.setdefault(test_name, result_time)
        print(result)
    return print("all tests completed")


make_test()
for name, secs in time_result.items():
    print(f"{name}: {secs:.8f} сек")
