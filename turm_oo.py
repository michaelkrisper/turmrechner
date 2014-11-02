import sys


class Tower():
    def __init__(self, number):
        self.number = number

    def __str__(self):
        nr = number
        lines = []
        pad = len(str(nr * 362880)) + 1

        for multiplikator in range(2, 10):
            lines.append("{number:{pad}} * {fac}".format(pad=pad, number=nr, fac=multiplikator))
            nr *= multiplikator

        for divident in range(2, 10):
            lines.append("{number:{pad}} / {fac}".format(pad=pad, number=nr, fac=divident))
            nr //= divident

        lines.append("{number:{pad}}".format(pad=pad, number=number))
        return "\n".join(lines)


number = int(sys.argv[1])
print(Tower(number))

