
# 时间复杂度O(1)
# x存在set中，就返回True，否则返回False


def find(st:set,x:int)->bool:
    if x in st:
        return True
    else:
        return False

# set不限制数据类型
st = set()
st.add(1)
st.add('one')
st.add(2.0)
print(st)

print(find(st,'one'))
