#이진탐색
import sys
input=sys.stdin.readline
n,m=map(int,input().split())
li=list(map(int,input().split()))
li.sort(reverse=True)
def bs(start,end):
    if start==end:
        return start
    mid=(start+end)//2
    total=0
    for i in range(n):
        if li[i]-mid>=0:
            total+=li[i]-mid
        else:
            break
    if total>=m:
        start=mid
    else:
        end=mid
    if end-start==1:
        return start
    return bs(start,end)
print(bs(0,li[0]))
