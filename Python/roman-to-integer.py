#!/usr/bin/env python3

"""Roman to Integer
https://leetcode.com/problems/roman-to-integer/
"""

symbol_map = {
    'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000
}

class Solution:
    def romanToInt(self, symbol):
        value = 0
        for i in range(0, len(symbol)):
            if i+1 < len(symbol) and symbol_map[symbol[i+1]] > symbol_map[symbol[i]]:
                value -= symbol_map[symbol[i]]
            else:
                value += symbol_map[symbol[i]]
        return value


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

            ret = Solution().romanToInt(s)

            out = str(ret)
            print(out)
        except StopIteration:
            break


if __name__ == '__main__':
    main()
