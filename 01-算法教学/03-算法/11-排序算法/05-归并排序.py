'''
时间复杂度: O(nlogn)
空间复杂度: O(n)
'''

def merge_sort(A:list[int],l:int,r:int):
    if r - l + 1 <= 1:
        return
    mid = (l + r)//2
    merge_sort(A,l, mid) # [l,mid]
    merge_sort(A,mid+1,r) # [mid+1,r]
    i = l
    j = mid + 1
    sorted = []
    while i <= mid and  j <= r:
        if A[i] < A[j]:
            sorted.append(A[i])
            i += 1
        else:
            sorted.append(A[j])
            j += 1
    while i <= mid:
        sorted.append(A[i])
        i += 1
    while j <= r:
        sorted.append(A[j])
        j += 1
    for i in range(l,r + 1):
        A[i] = sorted[i - l]

A = [1,2,3,6,7,9,12,4,5,9,1,2,3,2,1]
merge_sort(A,0,len(A)-1)
print(A)