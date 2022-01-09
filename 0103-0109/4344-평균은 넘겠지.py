n=int(input())
ans=[]
for _ in range(n):
    num=list(map(int,input().split()))#실수한 부분
    for i in range(n):
            sum=0
            stunum=0
            for j in range(1,len(num)):
                sum+=num[j]
            average=sum/num[0]
            for j in range(1,len(num)):
                if num[j]>average:
                    stunum+=1
    print("{:.3f}%".format(stunum/(len(num)-1)*100))
    
