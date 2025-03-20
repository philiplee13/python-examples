import time
from concurrent.futures import ProcessPoolExecutor


def main():
    synchronous()
    multiprocessed()


def synchronous():
    start_time = time.perf_counter()
    for _ in range(20):
        fib(35)
    duration = time.perf_counter() - start_time
    print(f"Synchronous: Computed in {duration} seconds")


def multiprocessed():
    start_time = time.perf_counter()
    with ProcessPoolExecutor(max_workers=5) as executor:
        executor.map(fib, [35] * 20)
    duration = time.perf_counter() - start_time
    print(f"Multiprocessing: Computed in {duration} seconds")


def fib(n):
    return n if n < 2 else fib(n - 2) + fib(n - 1)


if __name__ == "__main__":
    main()
