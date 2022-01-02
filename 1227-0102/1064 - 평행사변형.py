import math
a,b,c,d,e,f=map(int,input().split())
if (a-c)==0:
    s1=(a-c)/(b-d)
else:
    s1=(b-d)/(a-c)
if (c-e)==0:
    s2=(c-e)/(d-f)
else:
    s2=(d-f)/(c-e)


li=[]
if s1==s2:
    print(-1.0)
else:
    temp1=math.sqrt((a-c)**2+(b-d)**2)*2
    temp2=math.sqrt((c-e)**2+(d-f)**2)*2
    temp3=math.sqrt((e-a)**2+(f-b)**2)*2
    li.append(temp1+temp2)
    li.append(temp2+temp3)
    li.append(temp3+temp1)
    print(max(li)-min(li))
