from functools import wraps
from typing import Any, Callable


def log(filename: str = "console") -> Callable:
    """Декоратор для логирования вызова функции в текстовый файл или консоль."""
    def decorator(func: Callable) -> Callable:
        @wraps(func)
        def wrapper(*args: Any, **kwargs: Any) -> Any:
            try:
                result = func(*args, **kwargs)
                message = f"{func.__name__} ok."
            except Exception as e:
                message = f"{func.__name__} error: {e}. Inputs: {args}, {kwargs}"
                result = None
            if ".txt" in filename:
                with open(filename, "a", encoding="utf-8") as file:
                    file.write(f"\n{message}")
            else:
                print(message)
            return result

        return wrapper

    return decorator
