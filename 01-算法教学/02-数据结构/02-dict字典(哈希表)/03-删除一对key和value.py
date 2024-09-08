
# keyError: 一般都是访问、删除一个不存在的key
# TypeError: 出现的很少，不可哈希的情况：TypeError: unhashable type: 'list'
# 时间复杂度O(1)
# del是一个关键词，不是一个函数
# del 是删除key-value
def remove(table:dict,k)->dict:
    if k in table:
        del table[k]
    return table

