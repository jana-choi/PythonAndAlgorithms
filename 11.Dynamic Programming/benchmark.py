from functools import wraps
import time

def benchmark(method):
    @wraps(method)
    def timed(*args, **kw):
        ts = time.time()
        result = method(*args, **kw)
        te = time.time()
        print("{0}: {1:0.2f} ms".format(method.__name__, ((te-ts)*1000)))
        return result
    return timed