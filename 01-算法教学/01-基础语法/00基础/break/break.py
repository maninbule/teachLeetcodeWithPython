

'''
break： 跳出离自己最近的一个for循环
'''

for i in range(10):
    for j in range(10):
        if j == 5:
            break
        print(j,end=" ")
    print()

