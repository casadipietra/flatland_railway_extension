from functools import lru_cache

import numpy as np


@lru_cache()
def min_cached(a, b):
    return min(a, b)


@lru_cache()
def max_cached(a, b):
    return max(a, b)


@lru_cache()
def ceil_cached(a):
    return int(np.ceil(a))
