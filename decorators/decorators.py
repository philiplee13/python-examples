def main():
    # decorated_method = decorator(say_whee)  # <- this is a bit odd looking
    # in the wild - people often use the pie syntax
    say_whee()

    greet("tobi")
    slow_method(2)


"""
Simple example of decorators
"""


def decorator(func):
    def wrapper():
        print("Something is happening before the function is called.")
        func()
        print("Something is happening after the function is called.")

    return wrapper


@decorator  # <- adding the @ is the same as line 4 above
def say_whee():
    print("Whee!")


def do_twice(func):
    def wrapper_do_twice(*args, **kwargs):  # <- how to use decorators with args
        func(*args, **kwargs)
        func(*args, **kwargs)

    return wrapper_do_twice


@do_twice
def greet(name):
    print(f"Hello {name}")


"""
A real world example of timing methods
"""
import functools
import time


def timer(func):
    """Print the runtime of the decorated function"""

    @functools.wraps(func)
    def wrapper_timer(*args, **kwargs):
        start_time = time.perf_counter()
        value = func(*args, **kwargs)
        end_time = time.perf_counter()
        run_time = end_time - start_time
        print(f"Finished {func.__name__}() in {run_time:.4f} secs")
        return value

    return wrapper_timer


@timer
@do_twice  # if you use multiple decorators - you need to make sure they either all take args or not
# if I try to use the original @decorator here it won't work
def slow_method(x):
    time.sleep(x)
    print(f"finished sleeping for {x}")


if __name__ == "__main__":
    main()
