import time


def decorator(func):
    def wrapper(*params, **kwargs):
        start_time = time.time()
        func(*params, **kwargs)
        end_time = time.time()
        print(f'{func.__name__} was running for {end_time-start_time}')
        return result
    return wrapper

def cache(func):
    cache = {}

    def wrapper(*args):
        if args in cache:
            return cache[args]
        cache[args] = func(*args)

        return cache[args]
    wrapper.cache = cache
    return wrapper

@decorator
def hard_fu():
    time.sleep(3)
    print("func done")

def main():
    hard_fu()

if __name__  == __main__
    main()
