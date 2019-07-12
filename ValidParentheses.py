# 20
# S
# 给定一个只包括 '('，')'，'{'，'}'，'['，']' 的字符串，判断字符串是否有效。
# 有效字符串需满足：
# 左括号必须用相同类型的右括号闭合。
# 左括号必须以正确的顺序闭合。
# 注意空字符串可被认为是有效字符串。

# 示例 1:
# 输入: "()"
# 输出: true

# 示例 2:
# 输入: "()[]{}"
# 输出: true

# 示例 3:
# 输入: "(]"
# 输出: false

# 示例 4:
# 输入: "([)]"
# 输出: false

# 示例 5:
# 输入: "{[]}"
# 输出: true

class Solution:
    def isValid(self, s: str) -> bool:
        sLen = len(s)
        if sLen <= 0:
            return True
        dict = {
            '(':0, ')':1,
            '[':2, ']':3,
            '{':4, '}':5
        }
        stack = []
        for i in range(sLen):
            if len(stack) <= 0:
                stack.append(s[i])
                continue
            c1 = s[i]
            c2 = stack[-1]
            if c1 in dict and c2 in dict:
                if dict[c1] - dict[c2] == 1:
                    stack.pop()
                else:
                    stack.append(c1)
        return len(stack) <= 0

s = Solution()
a = s.isValid("()")
print(a)
a = s.isValid("()[]{}")
print(a)
a = s.isValid("(]")
print(a)
a = s.isValid("([)]")
print(a)
a = s.isValid("{[]}")
print(a)