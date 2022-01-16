o=-1;w=-1
num=1
while(True):
    o,w=map(int,input().split())
    if(o==0 and w==0):
        break
    temp1='-1';temp2='-1'
    flag=True
    while(True):
          temp1,temp2=map(str,input().split())
          if (temp1=='#' and temp2=='0'):
              break
          if temp1=='F':
              w+=int(temp2)
          else:
              w-=int(temp2)
          if w<=0:
              flag=False
    if flag==False:
        print(num,'RIP')
    else:
        if w>o*0.5 and w<o*2:
            print(num,':-)')
        else:
            print(num,':-(')
    num+=1
