#index(i)쓰는거
#같은 수가 두 개 이상 있을 때 처리방법
#->인덱스 만들고 숫자 증가시킴
n=int(input())
li=list(map(int,input().split()))
temp=[0]*1001
newli=[]
for i in li:
    newli.append(i)#newli=li하고 newli.sort하니깐 li도 오름차순 정렬됨 왜??
newli.sort()
num=0
for i in li:
    if li.count(i)>1:
        print(newli.index(i)+temp[i],end=" ")
        temp[i]=temp[i]+1
    else:
        print(newli.index(i),end=" ")
