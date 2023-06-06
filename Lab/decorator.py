def limit_calls(max_calls):
    def decorator(func):
        calls = 0

        def wrapper(*args, **kwargs):
            nonlocal calls
            if calls < max_calls:
                calls += 1
                return func(*args, **kwargs)
            else:
                raise Exception("Too many calls")

        return wrapper

    return decorator


def count_arguments(func):
    def wrapper(*args, **kwargs):
        num_args = len(args)
        num_kwargs = len(kwargs)
        print(f"Number of arguments: {num_args}")
        print(f"Number of keyword arguments: {num_kwargs}")
        return func(*args, **kwargs)

    return wrapper
