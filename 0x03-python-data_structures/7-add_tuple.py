#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    res = tuple(map(sum, zip(tuple_a, tuple_b)))
    return res
