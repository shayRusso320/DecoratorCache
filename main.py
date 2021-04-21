import pickle
cache = {}


def save_obj(obj, name):
    with open('obj/' + name + '.pkl', 'wb') as f:
        pickle.dump(obj, f, pickle.HIGHEST_PROTOCOL)


def load_obj(name):
    with open('obj/' + name + '.pkl', 'rb') as f:
        return pickle.load(f)


def heavy_function(parameters):
    print("called")
    return 1


def call_function(parameters):
    # check if the function is called with these parameters for the first time
    if parameters not in cache.keys():
        # saving the result in the cache
        cache[parameters] = heavy_function(parameters)

    return cache[parameters]


# loading the cache from recent runs
try:
    cache = load_obj("cache")
except EOFError:
    cache = {}

print(call_function(4))
print(call_function(4))
print(call_function(3))
print(call_function(2))

# saving the cache into the file, for use in future runs
save_obj(cache, "cache")
