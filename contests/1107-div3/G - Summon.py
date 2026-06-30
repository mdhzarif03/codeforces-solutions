import sys
from math import gcd

input = sys.stdin.readline

t = int(input())

for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))

    ans = 0
    dp = {}

    for x in a:
        ndp = {(x, x): 1}

        for (g, first), cnt in dp.items():
            ng = gcd(g, x)
            key = (ng, first)
            ndp[key] = ndp.get(key, 0) + cnt

        for (g, first), cnt in ndp.items():
            ans += (first - g) * cnt

        dp = ndp

    print(ans)