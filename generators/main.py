import tracemalloc


def naive_generator(limit):
    num = 0
    while num < limit:
        print(num)
        num += 1


def number_generator(limit):
    num = 0
    while num < limit:
        yield num
        num += 1


def main():
    tracemalloc.start()
    naive_generator(10000000)
    current, peak = tracemalloc.get_traced_memory()
    tracemalloc.stop()
    print(f"Current memory usage for naive: {current / 10**6}MB")
    print(f"Peak memory usage for naive: {peak / 10**6}MB")

    ## generator
    tracemalloc.start()
    number_generator(1000000)
    current, peak = tracemalloc.get_traced_memory()
    tracemalloc.stop()
    print(f"Current memory usage for generator: {current / 10**6}MB")
    print(f"Peak memory usage for generator: {peak / 10**6}MB")


if __name__ == "__main__":
    main()
