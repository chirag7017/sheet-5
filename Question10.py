# Reverse
# Given and array A, Find the reverse of it. (Solve thos question with for loop)

A=[3,5,1,2,1,2]
B=[]
for i in range(len(A)-1,-1,-1):
    B.append(A[i])
print(B)