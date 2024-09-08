
'''
遍历dict:
有3种方式

key-value

# .items只是在dict 同时for循环key-value的时候使用
'''

# 时间复杂度O(n)
def trverseDict():
    my_dict = {'a': 1, 'b': 2, 'c': 3}
    # 只遍历key
    for key in my_dict.keys():
        print(key,end=" ")
    print()
    # 只遍历value
    for value in my_dict.values():
        print(value,end=" ")
    print()
    # 同时遍历key和value
    for key, value in my_dict.items(): # 每一轮产生一个(key,value)
        print("(",key, value,end=" ) ")
        break

trverseDict()