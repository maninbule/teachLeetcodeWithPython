


'''
1. 字符串不可以修改
2. 访问机制和数组是一样的
'''
'''
反转字符串
'''

def reverse_string(s):
    return s[::-1]

'''
切分字符串
'''
def split_string(s, delimiter):
    return s.split(delimiter)

'''
字符串拼接
'''

def custom_join(strings, delimiter):
    return delimiter.join(strings)

'''
取子字符串
'''
def slice_string(s, start, end):# [start,end)
    return s[start:end]

'''
修改字符串某个区间，让他翻转
'''
s = "123456"
start = 2
end = 5
s = s[:start] + s[start:end][::-1] + s[end:]
print(s)

