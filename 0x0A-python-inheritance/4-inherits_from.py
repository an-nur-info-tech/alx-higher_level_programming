#!/usr/bin/python3


def inherits_from(obj, a_class):
    """function"""
    result = isinstance(obj, a_class) and type(obj) is not a_class
    return result
