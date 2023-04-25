from collections.abc import Callable

def cache(times: int) -> Callable:
    def decorator(func: Callable) -> Callable:
        cache = {}

        def wrapper(*args, **kwargs):
            if cache.get(args) is None or cache[args][1] == 0:
                func_result = func(*args, **kwargs)
                cache[args] = (func_result, times - 1)
                return func_result
            else:
                cache[args] = (cache[args][0], cache[args][1] - 1)
                return cache[args][0]

        return wrapper
    return decorator


#ТЕСТЫ:

#1ТЕСТ
@cache(times=3)
def f():
    return input('? ')

print(f())
print(f())
print(f())
print(f())
print(f())
print(f())


#2ТЕСТ
@cache(times=2)
def f():
    return input('? ')

print(f())
print(f())
print(f())
print(f())



#3ТЕСТ
@cache(times=4)
def f():
    return input('? ')

print(f())
print(f())
print(f())
print(f())
