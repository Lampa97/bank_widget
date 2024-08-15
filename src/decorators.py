from time import time


def log(filename=''):
    def decorator(func):
        def wrapper(*args, **kwargs):
            try:
                start_time = time()
                result = func(*args, **kwargs)
                end_time = time()
                run_time = end_time - start_time
                message = f'{func.__name__} ok. Runtime: {run_time}'
            except Exception as e:
                message = f'{func.__name__} error: {e}. Inputs: {args}, {kwargs}'
                result = None
            if filename:
                with open(filename, 'a', encoding='utf-8') as file:
                    file.write(f"\n{message}")
            else:
                print(message)
            return result
        return wrapper
    return decorator
