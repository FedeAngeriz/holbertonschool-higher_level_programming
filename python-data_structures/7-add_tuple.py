#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    tuple_a = tuple_a + (0,) * (len(tuple_b) - len(tuple_a))
    tuple_b = tuple_b + (0,) * (len(tuple_a) - len(tuple_b))
    return tuple(t1 + t2 for t1, t2 in zip(tuple_a, tuple_b))
