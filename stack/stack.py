# Valid Parentheses

from constat import (
    data_1,
    data_2,
    data_3,
    data_4,
    data_5,
)


def is_valid(data: str) -> bool:
    stack = []
    pairs = {
        '[': ']',
        '{': '}',
        '(': ')',
    }

    for char in data:
        if char in pairs:
            stack.append(char)
        else:
            if not stack:
                return False
            last = stack.pop()
            if char != pairs[last]:
                return False

    return not stack


def make_test():
    data: list[str] = [
        data_1,
        data_2,
        data_3,
        data_4,
        data_5,
    ]

    for incoming_data in data:
        result = is_valid(incoming_data)
        print(result)
    return print("all tests completed")


make_test()

