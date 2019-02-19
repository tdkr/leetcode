#!/usr/bin/env python3

"""String To Integer(atoi)
https://leetcode.com/problems/string-to-integer-atoi/
"""

Max_Int32 = 2**31-1
Min_Int32 = 0 - 2**31

class Solution:
    def myAtoi(self, str_val: 'str'):
        val = 0
        sign = -1  # 0 for Negative and 1 for Positive
        for ch in str_val.lstrip():
            if sign == -1:
                if ch == '-':
                    sign = 0
                    continue
                elif ch == '+':
                    sign = 1
                    continue
                if ch >= '0' and ch <= '9':
                    sign = 1
                else:
                    return 0
            elif ch < '0' or ch > '9':
                break

            val = val * 10 + (ord(ch) - ord('0'))

        if sign == 0:
            val = 0 - val
            if val < Min_Int32:
                val = Min_Int32
        else:
            if val > Max_Int32:
                val = Max_Int32

        return val


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
            lineStr = stringToString(line)

            ret = Solution().myAtoi(lineStr)

            out = str(ret)
            print(out)
        except StopIteration:
            break


if __name__ == '__main__':
    main()
