
# 时间复杂度O(1)

# 注意1： 删除元素的时候，一定要确定他在集合中
# 注意2： 集合和字典，集合是存储key，字典是存储key-value
def remove(st:set,x):
    st.remove(x)

# key - value
st = {'2','3'}
if '1' in st:
    st.remove('1') # key
print(st)