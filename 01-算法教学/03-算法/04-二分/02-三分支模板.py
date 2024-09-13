

'''
给一个数组，通过二分查找target所在的索引
如果索引不存在，就返回-1
'''

def findTarget(nums:list[int],target:int)->int:
    left, right = 0, len(nums) - 1
    ans = -1
    while left <= right:
        mid = (left + right) // 2
        if nums[mid] == target:
            return mid
        elif nums[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return ans

nums = [1,2,3,5,8,9,9,10,30,78,560]
index = findTarget(nums,8)
print(index)