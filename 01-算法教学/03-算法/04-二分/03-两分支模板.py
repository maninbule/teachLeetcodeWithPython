
def findTarget(A:list[int],target:int)->int:
    l, r, ans = 0, len(A)-1, -1
    while l <= r:
        mid = (l + r) // 2
        if A[mid] <= target:
            ans = mid
            l = mid + 1
        else:
            r = mid - 1
    if ans == -1 or A[ans] != target:
        return -1
    else:
        return ans

A = [1,2,3,5,8,9,9,9,9,30,78,560]

index = findTarget(A,10)
print(index)

