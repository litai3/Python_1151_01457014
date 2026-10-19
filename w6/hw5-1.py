def memoize_decorator(func):
    cache = {}

    def warpper(n):
        if n in cache.keys():
            print(f"Cache hit for fibonacci({n})")
            return cache[n]

        result = func(n)
        print(f"Computed fibonacci({n}) = {result}")
        cache[n] = result
        return result

    return warpper


@memoize_decorator
def fibonacci(n):
    if n <= 1:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)


if __name__ == "__main__":
    n = int(input())
    ans = fibonacci(n)
    print(f"Final Result: {ans}")
