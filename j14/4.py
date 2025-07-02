# def fact(n):
#     if n == 1:
#         return 1
#     else:
#         return n * fact(n-1)

# print(fact(40))

def memoize(func):
    cache = {}
    def wrapper(*args, **kwargs):
        if args in cache:
            return cache[args]
        result = func(*args, **kwargs)
        cache[args] = result
        return result
    return wrapper

@memoize
def fibonacci(n):
    if n==1 or n==2:
        return 1
    return fibonacci(n-1) + fibonacci(n-2)

print(fibonacci(450))
