

# 时间复杂度O(n)

# set遍历的时候，是不能使用索引，因为set是无序的
def traverse_set(st:set):
    for x in st:
        print(x)
