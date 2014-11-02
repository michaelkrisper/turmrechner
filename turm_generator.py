import sys
import operator


def calc(number, *args):
    for opstr, op in args:
        for fac in range(2, 10):
            yield (number, opstr, fac)
            number = op(number, fac)
    yield (number, "", "")


nr = int(sys.argv[1])
pad = len(str(nr * 362880)) + 1

for number, op, fac in calc(nr, (" * ", operator.mul), (" / ", operator.floordiv)):
    print("{number:{pad}}{op}{fac}".format(pad=pad, op=op, number=number, fac=fac))