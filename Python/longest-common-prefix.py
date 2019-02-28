#!/usr/bin/env python3

"""Longest-Common-Prefix
https://leetcode.com/problems/longest-common-prefix/
"""

class Solution:
    def longestCommonPrefix(self, strs: 'List[str]') -> 'str':
        if len(strs) == 0:
            return ""
        firstStr = strs[0]
        for index in range(0, len(firstStr)):
            ch = firstStr[index]
            for i in range(1, len(strs)):
                matchStr = strs[i]
                if index >= len(matchStr) or matchStr[index] != ch:
                    return firstStr[0:index]
        return firstStr

print(Solution().longestCommonPrefix([
    # "flower", "flow", "flight",
    "dog","racecar","car"
]))
