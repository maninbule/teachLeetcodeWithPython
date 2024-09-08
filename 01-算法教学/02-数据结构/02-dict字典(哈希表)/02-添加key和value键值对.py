
# 时间复杂度O(1)

# key只能是int,str,tuple, 不能是list
# key是不能改变的
# tuple可以用于记录坐标，就是一组数去映射一个value
def add(table:dict,k,v)->dict:
    table[k] = v
    return table

table = dict()

table[1] = 'one'
table[2] = 'two'
print(table)

table[(1,2,3)] = 'x'
print(table)
