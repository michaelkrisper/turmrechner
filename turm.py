#!/usr/bin/python3
# coding=utf-8
"""Script for calculating a numeric tower.

Usage:
$ python3 turm.py [number]
number : the starting number. Must be greater than 0.

Example:
$ python3 turm.py 5
       5 * 2
      10 * 3
      30 * 4
     120 * 5
     600 * 6
    3600 * 7
   25200 * 8
  201600 * 9
 1814400 / 2
  907200 / 3
  302400 / 4
   75600 / 5
   15120 / 6
    2520 / 7
     360 / 8
      45 / 9
       5
"""
import sys

__author__ = "Michael Krisper"
__email__ = "michael.krisper@tugraz.at"
__updated__ = "2014-11-02"


def main(number):
    """
    Main Function
    :param number: the starting number
    """

    pad = len(str(number * 362880)) + 1

    for multiplikator in range(2, 10):
        print("{number:{pad}} * {fac}".format(pad=pad, number=number, fac=multiplikator))
        number *= multiplikator

    for divident in range(2, 10):
        print("{number:{pad}} / {fac}".format(pad=pad, number=number, fac=divident))
        number //= divident

    print("{number:{pad}}".format(pad=pad, number=number))


if __name__ == "__main__":
    if len(sys.argv) == 1:
        print(__doc__)
        sys.exit()

    try:
        main(int(sys.argv[1]))
    except ValueError:
        print("Error while converting the argument to an integer.")