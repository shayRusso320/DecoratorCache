import pickle

cache = {}


def save_obj(obj, name):
    with open('obj/' + name + '.pkl', 'wb') as f:
        pickle.dump(obj, f, pickle.HIGHEST_PROTOCOL)


def load_obj(name):
    with open('obj/' + name + '.pkl', 'rb') as f:
        return pickle.load(f)


def cache_decorator(func):

    def inner(parameters):

        if parameters not in cache.keys():  # check if the function is called with these parameters for the first time
            cache[parameters] = func(parameters)  # saving the result in the cache

        return cache.get(parameters)

    return inner


@cache_decorator
def heavy_function(parameters):
    print("called")
    return 1


# loading the cache from recent runs
try:
    cache = load_obj("cache")
except EOFError:
    cache = {}

print(heavy_function(4))
print(heavy_function(4))
print(heavy_function(3))
print(heavy_function(2))

# saving the cache into the file, for use in future runs
save_obj(cache, "cache")
