import sys
import operator
import itertools

nr = int(sys.argv[1])
max_nr = nr * 362880
pad = len(str(max_nr)) + 1

for number, op, fac in itertools.chain(
        zip(itertools.accumulate(itertools.chain((nr,), range(2, 10)), operator.mul), itertools.repeat(" * "), range(2, 10)),
        zip(itertools.accumulate(itertools.chain((max_nr,), range(2, 10)), operator.floordiv), itertools.repeat(" / "), range(2, 10)),
        ((nr, "", ""),)):
    print("{number:{pad}}{op}{fac}".format(pad=pad, op=op, number=number, fac=fac))