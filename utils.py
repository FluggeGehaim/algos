from time import perf_counter


def get_time(func):
    def wrapper(*args, **kwargs):
        start_time = perf_counter()
        result = func(*args, **kwargs)
        result_time = (perf_counter() - start_time)
        return result, result_time

    return wrapper
