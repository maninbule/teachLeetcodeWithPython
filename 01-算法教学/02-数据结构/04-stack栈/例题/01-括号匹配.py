
'''
https://leetcode.cn/problems/valid-parentheses/description/
'''

class Solution:
    def isValid(self, s: str) -> bool:
        sk = []
        for c in s:
            if c == ']' or c == '}' or c == ')':
                if len(sk) == 0:
                    return False
                left = sk[-1]
                if c == ']' and left != '[':
                    return False
                if c == ')' and left != '(':
                    return False
                if c == '}' and left != '{':
                    return False
                sk.pop()
            else:
                sk.append(c)
        # 上面右括号都匹配了左括号，但是可以还有剩余的左括号
        if len(sk) == 0:
            return True
        else:
            return False

'''
3种不匹配的情况：
1. 遇到右括号的时候，栈里面没有左括号
2. 有左括号，但是不匹配
3. 右括号都匹配了左括号，但是可以还有剩余的左括号
'''

# 优化1
class Solution:
    def isValid(self, s: str) -> bool:
        sk = []
        for c in s:
            if c in ']})':
                if len(sk) == 0:
                    return False
                left = sk[-1]
                if c == ']' and left != '[':
                    return False
                if c == ')' and left != '(':
                    return False
                if c == '}' and left != '{':
                    return False
                sk.pop()
            else:
                sk.append(c)
        # 上面右括号都匹配了左括号，但是可以还有剩余的左括号
        return len(sk) == 0

'''
3种不匹配的情况：
1. 遇到右括号的时候，栈里面没有左括号
2. 有左括号，但是不匹配
3. 右括号都匹配了左括号，但是可以还有剩余的左括号
'''


class Solution:
    def isValid(self, s: str) -> bool:
        sk = []
        # key是右括号，value是左括号
        table = {']':'[','}':'{',')':'('}
        for c in s:
            if c in table.keys():
                if len(sk) == 0:
                    return False
                left = sk[-1]
                should = table[c]
                if left != should:
                    return False
                sk.pop()
            else:
                sk.append(c)
        # 上面右括号都匹配了左括号，但是可以还有剩余的左括号
        return len(sk) == 0

'''
3种不匹配的情况：
1. 遇到右括号的时候，栈里面没有左括号
2. 有左括号，但是不匹配
3. 右括号都匹配了左括号，但是可以还有剩余的左括号
'''