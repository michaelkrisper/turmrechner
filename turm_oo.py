#!/usr/bin/python3
# coding=utf-8
"""
Script for displaying a numeric tower.
"""

import sys

__author__ = "Michael Krisper"


class Tower():
    """
    A class representing a numeric tower.
    @param number: the number to start with
    """
    def __init__(self, number):
        self._number = number
        self._items = None

    def __iter__(self):
        def it(nr):
            for fac in range(2, 10):
                yield (nr, " * ", fac)
                nr *= fac

            for fac in range(2, 10):
                yield (nr, " / ", fac)
                nr //= fac
            yield (nr, "", "")

        return it(self._number)

    def __getitem__(self, item):
        if not self._items:
            self._items = list(iter(self))
        return self._items[item]

    def __str__(self):
        pad = len(str(self._number * 362880)) + 1
        return "\n".join(
            "{number:{pad}}{op}{fac}".format(pad=pad, op=op, number=nr, fac=fac) for nr, op, fac in iter(self))

    def __repr__(self):
        return "Tower({})".format(self._number)


def main():
    number = int(sys.argv[1])
    t = Tower(number)
    print(t)


if __name__ == "__main__":
    main()