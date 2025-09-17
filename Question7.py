# Separate Odd Even
# You are given an integer array A.
# You have to print the odd and even elements of array A in 2 seprate lines.

A=[1,2,3,4,5]
even=[]
odd=[]
for i in A:
    if i%2==0:
        even.append(i)
    else:
        odd.append(i)
print(*odd)