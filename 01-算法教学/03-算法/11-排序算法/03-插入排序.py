'''
O(n^2)
'''



def insert_sort(A:list[int]):
    n = len(A)
    for i in range(1,n):
        for j in range(i-1,-1,-1):
            if A[j] > A[j + 1]:
                A[j],A[j + 1] = A[j + 1],A[j]
            else:
                break

A = [1,2,3,6,7,9,12,4,5,9,1,2,3,2,1]
insert_sort(A)
print(A)