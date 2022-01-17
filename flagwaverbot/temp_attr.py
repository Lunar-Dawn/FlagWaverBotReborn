from typing import Any

from contextlib import contextmanager


@contextmanager
def temp_attr(x: Any, name: str, value: any):
    setattr(x, name, value)
    try:
        yield
    finally:
        delattr(x, name)
