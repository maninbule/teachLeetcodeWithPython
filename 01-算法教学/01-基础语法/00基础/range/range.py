

'''
range 可以认为是产生一个数组

range(start,end,step) 和 slice[start,end,step] 一样的

默认值range(0,end,1)
'''

for i in range(5): # [0,5)
    print(i,end=" ")
print()
for i in range(1,10,2):
    print(i,end=" ")
print()
for i in range(10,0,-1):
    print(i,end=" ")

