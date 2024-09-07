
'''
key：就是接受一个函数，这个函数一般用lambda表达式来产生
'''
# 从小到大排序
def sort_ascending(arr):
    arr.sort(key=lambda x: x) # 从小到大排序
    return arr

# 从大到小排序
def sort_descending(arr):
    arr.sort(key=lambda x: -x) # 从大到小排序
    return arr

# 根据第0个元素进行从小到大排序
def sort_tuple_ascending(lst):
    lst.sort(key=lambda item: item[0])
    return lst
# 先根据第0个元素从小到大排序，再按第1个元素从大到小排序
def sort_tuple_custom(lst):
    lst.sort(key=lambda x: (x[0], -x[1]))
    return lst


def sort_tuple_custom2(lst:list[list[int]]):
    # 其中的x就是list[list[int]]中的list[int]
    lst.sort(key=lambda x:-(x[0] + x[2]))
    return lst

A = [[0,0],[3,5],[2,5],[3,2]]
A.sort(key=lambda x:(x[1],x[0]))
print(A)


score = [[90,89,100],[67,78,32],[60,100,89]]
sort_tuple_custom2(score)
print(score)

