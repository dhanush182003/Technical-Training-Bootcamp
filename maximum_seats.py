
arr=['S','S','X','S','S','S','X','X','X']
max_seat=0
count=0
for i in range(len(arr)):
    if(arr[i]=='S'):
        count+=1
    else:
        count=0
    if(count>max_seat):
        max_seat=count
print(max_seat)
