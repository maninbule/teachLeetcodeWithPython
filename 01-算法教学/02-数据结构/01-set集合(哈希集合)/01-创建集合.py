

#  注意1： 自动去重功能

# 注意2： set不具备排序功能

# set的主要用途就是查询速度快
def create()->set:
    st = set()
    # 也可以写成st = {} 但是不建议
    return st
def create2()->set:
    st = {'1','2','3'}
    return st
# 根据已有的数组来创建集合
def createFromList(arr:list)->set:
    st = set(arr)
    return st

# 对一个数组进行去重
def solve(arr:list[int])->list[int]:
    res = list(set(arr))
    return res

arr = [1,5,3,3,4,5,5,1]
print(solve(arr))