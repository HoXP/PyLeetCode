# 28
# S
# 实现 strStr() 函数。
# 给定一个 haystack 字符串和一个 needle 字符串，在 haystack 字符串中找出 needle 字符串出现的第一个位置 (从0开始)。如果不存在，则返回  -1。

# 示例 1:
# 输入: haystack = "hello", needle = "ll"
# 输出: 2

# 示例 2:
# 输入: haystack = "aaaaa", needle = "bba"
# 输出: -1

class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        i = 0
        while True:
            j = 0
            while True:
                if j == len(needle):
                    return i
                if i + j == len(haystack):
                    return -1
                if needle[j] != haystack[i + j]:
                    break
                j = j + 1
            i = i + 1
            
s = Solution()
a = s.strStr("hello", "ll")
print(a)
a = s.strStr("aaaaa", "bba")
print(a)