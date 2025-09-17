# you are given a constant array A and B.
# you are required to return another array where Arr[ i] = arr[[ i]

Arr=[2,4,6,8]
B=3
Arr1=[]
for i in range(len(Arr)):
    Arr1.append(Arr[i]+B)
print(Arr1)