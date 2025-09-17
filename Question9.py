# Cube of Array
# you are provided with an integer array A. Return another array B of size same as the of Asuch thatB[i]=A[i]^3

A=[2,6,8,1]
B=[]
for i in A:
    B.append(i*i*i)
print(B)