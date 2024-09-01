def calc(t,e,l):
    currentguest=0
    maxguest=0
    for i in range(t):
        currentguest+=e[i]
        currentguest-=l[i]
        if maxguest<currentguest:
            maxguest=currentguest
    return maxguest
time=int(input("enter time in hours:"))
entry=[]
leave=[]
print("enter entries ")
for i in range(time):
    ele=int(input())
    entry.append(ele)
print("enter leaves ")
for i in range(time):
    ele=int(input())
    leave.append(ele)
print("maximum number of guest :",calc(time,entry,leave))

