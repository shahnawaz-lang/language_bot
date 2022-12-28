from itertools import compress
from collections import namedtuple

headers = namedtuple('properties', 'base pos function syntactic')


def formatter(string):
    string_props = {}
    for substrings in string.split('\n')[7:-2]:
        substrings = substrings.split()
        props = headers(*list(compress(substrings, [0, 0, 1, 1, 0, 1, 0, 1, 0])))
        string_props[substrings[1]] = f'`Base`={props.base} \n `POS`={props.pos} \n `function`={props.function} \n ' \
                                      f'`Syntactic`={props.syntactic} '
    return string_props
