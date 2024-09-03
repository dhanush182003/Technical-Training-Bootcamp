
n=int(input("enter the size of the array:"))
a=[]

for i in range(n):
    ele=int(input())
    a.append(ele)
def maxproduct(arr):
    max_product=0
    for i in range(len(arr)):
        for j in range(i+1,len(arr)):
            prod=arr[i]*arr[j]
            if prod>max_product:
                max_product=prod
    return max_product
print("maximum product of two elements in the array is :",maxproduct(a))

