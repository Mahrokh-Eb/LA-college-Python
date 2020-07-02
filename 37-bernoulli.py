# 2o ta seke 10000 bar baham bendaz
# 2ta adad migire, n= tedade sekeha, p= in azmayesh ro chan bar tekrar mikone
import sys
import math
import stddraw
import stdrandom
import stdstats
import gaussian

n = int(sys.argv[1])
trials = int(sys.argv[2])

freq = (n+1) * [0]
for t in range(trials):
    heads = stdrandom.binomial(n, 0.5)
    #n-ta seke partab kon, beshmor chanta shir miyad
    freq[heads] += 1

norm = [0.0] * (n+1)
for i in range(n+1):
    norm[i] = 1.0 * freq[i] / trials

#rasm tozi normal
phi = [0.0] * (n+1)
stddev = math.sqrt(n)/2.0
for i in range(n+1):
    phi[i] = gaussian.pdf(n, n/2, stddev)
stddraw.setCanvasSize(1000, 400 )
stddraw.setYscale(0, 1.0, max(max(norm), max(phi)))


