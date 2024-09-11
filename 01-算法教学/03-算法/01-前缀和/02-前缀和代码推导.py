
'''
也就是pre[i] = 求和A[j](其中j <=i)，第i个前缀和就是所有下标小于等于自己下标的原数组的元素和
通过上面，我们可以得出一个递推式
pre[0] = A[0]
之后的所有pre[i] = pre[i-1] + A[i]
 通过这个递推式，我们就可以用O(n)的复杂度求出前缀和数组
 '''

A = [1,3,2,6,7,8]

'''
传入一个普通的数组，返回一个前缀和数组
'''
def getPre(A:list)->list[int]:
    if A is None or len(A) == 0:
        return []
    pre = [0] * len(A)
    pre[0] = A[0]
    for i in range(1,len(A)):
        pre[i] = pre[i-1] + A[i] # 前i项的和 = 前i-1项的和 + 第i项的值 (i从0开始)
    return pre

# 测试
print(getPre(A))
