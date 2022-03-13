import sys

def count_star(n):
    ret = []
    for i in range(3*len(n)):
        if i//len(n) == 1:
            ret.append(n[i % len(n)] + " " * len(n) + n[i%len(n)])
        else:
            ret.append(n[i%len(n)]*3)
    return ret


n = int(sys.stdin.readline())
k = 0
star=["***","* *", "***"]
while n != 3:
    n//=3
    k+=1
for i in range(k):
    star = count_star(star)
for i in star:
    print(i)
