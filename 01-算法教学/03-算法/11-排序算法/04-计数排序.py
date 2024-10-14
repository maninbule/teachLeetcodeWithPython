'''
O(n + maxvalue)
'''
# [0,10,100,1000,10,20]


def sort(A:list[int])->list[int]:
    min_value = min(A)
    max_value = max(A)
    count = dict()
    for x in A: #O(n)
        if x not in count:
            count[x] = 1
        else:
            count[x] += 1
    result = []
    for i in range(min_value,max_value + 1): # O(max-min)
        if i in count:
            cnt = count[i]
            for j in range(cnt):
                result.append(i)
    return result
A = [1,2,3,6,7,9,12,4,5,9,1,2,3,2,1]
print(sort(A))

'''
time: O(n + (max-min))
space: O(max-min)
'''


