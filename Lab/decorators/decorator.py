"""
This is file contains decorator
"""
import logging


def limit_calls(max_calls):
    """
    This decorator limits the number of function calls
    """
    def decorator(func):
        calls = 0

        def wrapper(*args, **kwargs):
            nonlocal calls
            x = 7
            print(f"value: {x}")
            if calls < max_calls:
                calls += 1
                return func(*args, **kwargs)
            else:
                raise Exception("Too many calls")

        return wrapper

    return decorator


def count_arguments(func):
    """
    This decorator checks and prints the number of
    method arguments before calling it
    """
    def wrapper(*args, **kwargs):
        num_args = len(args) - 1
        num_kwargs = len(kwargs)
        print(f"Number of arguments: {num_args}")
        print(f"Number of keyword arguments: {num_kwargs}")
        return func(*args, **kwargs)

    return wrapper


def logged(exception, mode):
    def decorator(func):
        def wrapper(*args, **kwargs):
            try:
                return func(*args, **kwargs)
            except exception as exp:
                if mode == "console":
                    logging.error(str(exp))
                elif mode == "file":
                    logging.basicConfig(filename="error.log", level=logging.ERROR)
                    logging.error(str(exp))
                else:
                    raise ValueError("Invalid logging mode")

        return wrapper

    return decorator
