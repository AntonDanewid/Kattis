import sys
import math

for i in sys.stdin:
    ab = i.split()
    r = int(ab[0])
    c = int(ab[1])
    inner = r - c
    #Area for inner pizza without crust
    innerA = inner*inner
    #Area for whole pizza with crust
    outerA = r * r
    res = innerA / outerA
    res = res * 100
    #Format for significant number
    print(str.format('{0:.6f}', res))
