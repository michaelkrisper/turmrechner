import sys

number = int(sys.argv[1])
pad = len(str(number * 362880)) + 1

for multiplikator in range(2, 10):
    print("{number:{pad}} * {fac}".format(pad=pad, number=number, fac=multiplikator))
    number *= multiplikator

for divident in range(2, 10):
    print("{number:{pad}} / {fac}".format(pad=pad, number=number, fac=divident))
    number //= divident

print("{number:{pad}}".format(pad=pad, number=number))