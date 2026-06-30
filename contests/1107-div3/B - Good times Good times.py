import sys
input=sys.stdin.readline
t=int(input())
out=[]
for _ in range(t):
    x=input().strip()
    out.append(str(10**len(x)+1))
print('\n'.join(out))