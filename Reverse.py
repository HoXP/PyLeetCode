# 7
# S
# 给出一个 32 位的有符号整数，你需要将这个整数中每位上的数字进行反转。

# 示例 1:
# 输入: 123
# 输出: 321

# 示例 2:
# 输入: -123
# 输出: -321

# 示例 3:
# 输入: 120
# 输出: 21

# 注意:
# 假设我们的环境只能存储得下 32 位的有符号整数，则其数值范围为 [−231,  231 − 1]。请根据这个假设，如果反转后整数溢出那么就返回 0。
import sys

class Solution:
    def reverse(self, x: int) -> int:
        maxInt = 2**31-1
        minInt = -2**31
        if x > maxInt or x < minInt:
            return 0
        result = 0
        isNegative = False
        if x < 0:
            isNegative = True
            x = -x
        while x != 0:
            tail = x % 10
            newResult = result * 10 + tail
            if (newResult - tail) // 10 != result:
                return 0
            result = newResult
            x = x // 10
        result = isNegative and -result or result
        if result > maxInt or result < minInt:
            return 0
        return result

s = Solution()
a = s.reverse(120)
print(a)
a = s.reverse(-123)
print(a)
a = s.reverse(1534236469)
print(a)