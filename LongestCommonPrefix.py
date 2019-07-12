# 14
# S
# 编写一个函数来查找字符串数组中的最长公共前缀。
# 如果不存在公共前缀，返回空字符串 ""。

# 示例 1:
# 输入: ["flower","flow","flight"]
# 输出: "fl"
# 示例 2:
# 输入: ["dog","racecar","car"]
# 输出: ""
# 解释: 输入不存在公共前缀。

class Solution:
    def longestCommonPrefix(self, strs):
        if strs == None or len(strs) <= 0:
            return ""
        empty = ''
        minLen = len(strs[0])
        for i in range(1, len(strs)):
            iLen = len(strs[i])
            if minLen > iLen:
                minLen = iLen
        pre = []
        for i in range(minLen):
            for j in range(len(strs) - 1):
                if strs[j][i] != strs[j + 1][i]:
                    return empty.join(pre)
            pre.append(strs[0][i])
        if len(pre) > 0:
            return empty.join(pre)
        return ""

s = Solution()
a = s.longestCommonPrefix(["flower","flow","flight"])
print(a)
a = s.longestCommonPrefix(["dog","racecar","car"])
print(a)