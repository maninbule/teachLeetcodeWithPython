
'''
continue: 跳过当前的一次for循环

i % 2: 就是算i除以2的余数

'''

for i in range(10):
    # continue 跳到这里
    if i % 2 == 0:
        continue
    print(i)
