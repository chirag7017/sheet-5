# Even odd Elements
# For array A, you have to find the value of absolute diffrent between the counts of even and odd elemnts in the array.

A=[1,2, 3, 4]
even=0
odd=0
for i in A:
    if i%2==0:
        even=even+1
    else:
        odd=odd+1
print(abs(even-odd))
