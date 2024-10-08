'''
我们可以通过观察这个差分数组得到一些性质：
在差分数组中的每一个数，都表示自己以及后面的所有数都需要加上自己，才能还原成原数组的元素
所以差分数组中的元素ca[i],就是表示我想要对原数组的A[i~n]都加上ca[i]----重要

如何去表示对一个区间统一加一个数呢？
假如说我们想让要下标在区间[L,R]的元素统一加x，怎么操作呢？
我们知道ca[L] += x 就是对下标在L ~ n所有的元素统一加x,
可以知道我们多加了一部分，也就是R + 1 ~ n 这部分我们不应该加x的，
所以我们要减掉，我们我们再配合ca[R + 1] -= x就把多加的给抵消掉了。
所以对一个区间[L,R]统一加一个数就是
ca[L] + = x
ca[R + 1] -= x
注意：我们开辟的差分数组要比原数组大1，因为R的下标最大可以是n，但是这里由R + 1,
    为了下标不越界，所以我们差分数组开大一点。

差分主要用来做什么呢？
频繁地让数组的任意一个区间的所有元素同时加一个数，最终再查看这个原数组是什么样子。

假如说我们知道了一个数组A，数组的长度是n，然后有q次操作，
每次操作让数组下标在区间[L,R]的元素统一加一个数。
如果我们用暴力的方法来做，每次操作的时间复杂度就是O(n), 然后一共有q次操作，时间复杂度就是O(nq)
如果我们采用差分的方法来做，时间复杂度是多少呢？
首先处理出差分数组，时间复杂度O(n)，
之后每次循环就直接用一个式子ca[L] + = x, ca[R + 1] -= x就求出来了。
操作的时间复杂度就变成了O(1),最后再求最终数组(用前缀和)，
总的时间复杂度就是O(n + q + n) = O(n + q)。

可以看出O(n + q) 远远小于 O (nq)
'''