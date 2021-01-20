import functools
from datetime import datetime


def ticktock(func):
    @functools.wraps(func)
    def inner(*args, **kwargs):
        tick = datetime.now()
        for _ in range(10):
            _ = func(*args, **kwargs)
        tock = datetime.now()
        elapsed = tock - tick
        print(f"{elapsed.total_seconds() / 10:.4f} seconds per loop", flush=True)
        return func(*args, **kwargs)
    return inner