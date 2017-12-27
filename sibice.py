import sys
import math

matches = list()
bo = False
for i in sys.stdin:
    if bo is False:
        ab = i.split()
        w = int(ab[1])
        h = int(ab[2])
        diag = math.hypot(w, h)
        bo = True
    else:
        match = int(i)
        if match <= w or match <= h or match <= diag:
            print("DA")
        else:
            print("NE")