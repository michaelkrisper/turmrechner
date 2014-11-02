import sys


class Tower():
    def __init__(self, number):
        self.number = number

    def __iter__(self):
        def it(nr):
            for fac in range(2, 10):
                yield (nr, " * ", fac)
                nr *= fac

            for fac in range(2, 10):
                yield (nr, " / ", fac)
                nr //= fac
            yield (nr, "", "")
        return it(self.number)


    def __str__(self):
        lines = []
        pad = len(str(self.number * 362880)) + 1
        return "\n".join("{number:{pad}}{op}{fac}".format(pad=pad, op=op, number=nr, fac=fac) for nr, op, fac in iter(self))


number = int(sys.argv[1])
print(Tower(number))
