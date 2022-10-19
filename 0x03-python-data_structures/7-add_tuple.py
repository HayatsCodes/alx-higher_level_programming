#!/usr/bin/python3
# 7-add_tuple.py

def add_tuple(tuple_a=(), tuple_b=()):
    """Adds 2 tuples"""
    if len(tuple_a) < 2:
        a = [x for x in tuple_a]
        if len(tuple_a) < 1:
            a.append(0)
            a.append(0)
        else:
            a.append(0)
        tuple_a = tuple(a)
    if len(tuple_b) < 2:
        b = [x for x in tuple_b]
        if len(tuple_b) < 1:
            b.append(0)
            b.append(0)
        else:
            b.append(0)
        tuple_b = tuple(b)
    new_tuple = (tuple_a[0] + tuple_b[0], tuple_a[1] + tuple_b[1])
    return (new_tuple)
