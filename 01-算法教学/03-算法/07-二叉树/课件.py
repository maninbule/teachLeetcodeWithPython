''''''

'''
什么是二叉树?
二叉树其实相对于链表，其实就是链表节点只有一个指针，但是二叉树的节点中有两个指针，分别指向左右子树。

二叉树和链表都是笔试很少遇到，但是面试经常遇到。
由于二叉树和递归的关系十分紧密，所以我们这里就用二叉树来练习更加深入的学习递归。

二叉树节点的定义
class node:
  def __init__(self,val = 0,left = None,right = None):
    self.val = val
    self.left = left
    self.right = right

对于递归来说，我们一般会有2种在递归不同层之间传递信息的方法：
第一种：通过参数传递 (递归的时候，上层往下层通过**参数**传递信息)
第二种：通过返回值传递 (递归回溯的时候，下层往上层通过**返回值**传递信息)
'''