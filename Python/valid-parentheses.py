#!/usr/bin/env python3

"""Valid Parentheses
https://leetcode.com/problems/valid-parentheses/
"""

class Solution():
    def isValid(self, s: str):
        mp1 = {'(': ')', '[':']', '{':'}'}
        mp2 = {')': '(', ']':'[', '}':'{'}
        v_t = []
        for ch in s:
            if ch in mp1:
                v_t.append(ch)
            elif ch in mp2:
                if len(v_t) == 0:
                    return False
                if mp2[ch] == v_t.pop():
                    continue
                else:
                    return False
        return len(v_t) == 0

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
            
            ret = Solution().isValid(s)

            out = (ret)
            print(out)
        except StopIteration:
            break

if __name__ == '__main__':
    main()