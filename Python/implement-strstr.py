#!/usr/bin/env python3

"""Remove Duplicates from Sorted Array
https://leetcode.com/problems/remove-duplicates-from-sorted-array/
"""

class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        n1, n2 = len(haystack), len(needle)
        if n1 < n2:
            return -1
        if n1 == n2:
            return 0 if haystack == needle else -1
        for i in range(0, n1 - n2 + 1):
            if haystack[i:n2+i] == needle:
                return i
        return -1

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
            haystack = stringToString(line)
            line = next(lines)
            needle = stringToString(line)
            
            ret = Solution().strStr(haystack, needle)

            out = str(ret)
            print(out)
        except StopIteration:
            break

if __name__ == '__main__':
    main()