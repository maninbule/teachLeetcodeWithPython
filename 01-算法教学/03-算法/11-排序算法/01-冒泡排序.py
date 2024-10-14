'''
O(n^2)
'''
def bubble_sort(A:list[int]):
    n = len(A)
    for i in range(n): # 循环n趟冒泡的过程
        for j in range(n-i-1):
            if A[j] > A[j + 1]:
                A[j],A[j + 1] = A[j+1],A[j]

A = [1,2,3,6,7,9,12,4,5,9,1,2,3,2,1]
bubble_sort(A)
print(A)