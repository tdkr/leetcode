#!/usr/bin/env python3

"""Generate Parentheses
https://leetcode.com/problems/generate-parentheses/
"""

import math

class Solution:
    def generateParenthesis(self, n: int) -> 'List[str]':
        if n == 1:
            return ['()']

        result = []
        mark = {}
        subList = self.generateParenthesis(n-1)
        for str in subList:
            for i in range(0, math.ceil(len(str)/2)+1):
                s = str[:i] + "()" + str[i:]
                if s not in mark:
                    result.append(s)
                    mark[s] = True
        return result

print(Solution().generateParenthesis(3))