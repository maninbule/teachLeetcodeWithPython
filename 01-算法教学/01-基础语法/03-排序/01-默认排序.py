'''
• sort()是列表内置的方法，没有返回值，是将列表排序,列表变化了
• sorted是全局内置的方法，有返回值，返回对可迭代序列排序后的新对象，但是原来的序列不变
'''

# 从小到大排序
def ascending_sort(arr:list[int]):
    arr.sort()
    return arr

# 从大到小排序
def descending_sort(arr):
    arr.sort(reverse=True)
    return arr


