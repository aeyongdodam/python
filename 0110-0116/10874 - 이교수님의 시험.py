ans='1 2 3 4 5 1 2 3 4 5'
n=int(input())
for i in range(n):
    s=str(input())
    if s==ans:
        print(i+1)
