

def create()->set:
    st = set()
    # 也可以写成st = {} 但是不建议
    return st

# 根据已有的数组来创建集合
def createFromList(arr:list)->set:
    st = set(arr)
    return st