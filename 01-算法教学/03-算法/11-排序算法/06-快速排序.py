


import random
def sort(arr:list[int]):
    quick_sort(arr,0,len(arr)-1)
def quick_sort(arr:list[int],left:int,right:int):
    # 期望是left < right
    if left >= right:
        return
    # 去随机从[left,right]下标范围内找一个元素，作为基准
    index = random.randint(left,right)
    # 把基准放到left的位置，为了我们之后能够把基准放到中间去，放到左边，方便我们记住他的位置
    arr[index],arr[left] = arr[left],arr[index]
    pivot = arr[left]
    i = left # 实时指向小于等于基准的最后一个下标
    for j in range(left + 1,right + 1):
        if arr[j] <= pivot:
            i += 1
            arr[i],arr[j] = arr[j],arr[i]
    # [left,i] <= pivot, 且 arr[left] == pivot
    # [i + 1,right] >= pivot
    arr[left],arr[i] = arr[i],arr[left]
    # [left,i-1] <= pivot ,arr[i] == pivot,  [i + 1,right] > pivot
    # arr[i] == pivot 已经处于最终排序的正确位置了，就不用动了
    quick_sort(arr,left,i-1)
    quick_sort(arr,i + 1,right)

A = [1,2,3,6,7,9,12,4,5,9,1,2,3,2,1]
sort(A)
print(A)
