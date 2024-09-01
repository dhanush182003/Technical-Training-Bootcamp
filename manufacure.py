
vech=int(input("enter vechiles to be manufactured :"))
wheels=int(input("enter the number of wheels produced :"))
def manufacture(v,w):
    fw=(w-2*v)//2
    tw=v-fw
    return fw,tw
output=manufacture(vech,wheels)
print("four wheel manufacured :",output[0])
print("two wheel manufactured :",output[1])