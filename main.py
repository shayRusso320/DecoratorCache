cache = {}


def heavy_function(parameters):
    print("called")
    return 1


def call_function(parameters):
    # check if the function is called with these parameters for the first time
    if parameters not in cache.keys():
        # saving the result in the cache
        cache[parameters] = heavy_function(parameters)
    return cache[parameters]


print(call_function(4))
print(call_function(4))
print(call_function(3))
