'''
O(n^2)
'''



def select_sort(A:list[int]):
    n = len(A)
    for i in range(n):
        min_index = i
        for j in range(i,n):
            if A[j] < A[min_index]:
                min_index = j
        # 就找到了第i小元素的index，就把它交换到第i个位置上去
        A[min_index],A[i] = A[i],A[min_index]
A = [1,2,3,6,7,9,12,4,5,9,1,2,3,2,1]
select_sort(A)
print(A)