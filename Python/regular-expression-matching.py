#!/usr/bin/env python3

"""Regular Expression Matching
https://leetcode.com/problems/regular-expression-matching/
以 text 代表目标字符串， pattern 代表匹配字符串
dp(i, j) 表示 match(text[i:], pattern[j:])
不考虑 * 时可以逐位遍历比较
遇到 * 时则按如下处理:
前面字符串出现 0 次，match(text[i:], pattern[j+2:])
前面字符串出现 1 次以上，在当前字符匹配的基础上继续 match(text[i+1:], pattern[j:])
"""

class Solution:
    def isMatch(self, s: 'str', p: 'str'):
        mark = {}
        def dp(i, j):
            if (i, j) not in mark:
                is_match = False
                if j == len(p):
                    is_match = i == len(s)
                else:
                    first_match = i < len(s) and p[j] in {s[i], '.'}
                    if j + 1 < len(p) and p[j+1] == '*':
                        is_match = dp(i, j+2) or (first_match and dp(i+1, j))
                    else:
                        is_match = first_match and dp(i+1, j+1)
                mark[(i, j)] = is_match
            return mark[(i, j)]
        return dp(0, 0)

def stringToString(input):
    import json

    return json.loads(input)

def main():
    import sys
    import io
    def readlines():
        for line in io.TextIOWrapper(sys.stdin.buffer, encoding='utf-8'):
            yield line.strip('\n')

    lines = readlines()
    while True:
        try:
            line = next(lines)
            s = stringToString(line)
            line = next(lines)
            p = stringToString(line)
            
            ret = Solution().isMatch(s, p)

            out = (ret)
            print(out)
        except StopIteration:
            break

if __name__ == '__main__':
    main()