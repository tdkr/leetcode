"""String To Integer(atoi)
mplement atoi which converts a string to an integer.

The function first discards as many whitespace characters as necessary until the first non-whitespace character is found. Then, starting from this character, takes an optional initial plus or minus sign followed by as many numerical digits as possible, and interprets them as a numerical value.

The string can contain additional characters after those that form the integral number, which are ignored and have no effect on the behavior of this function.

If the first sequence of non-whitespace characters in str is not a valid integral number, or if no such sequence exists because either str is empty or it contains only whitespace characters, no conversion is performed.

If no valid conversion could be performed, a zero value is returned.

Note:

Only the space character ' ' is considered as whitespace character.
Assume we are dealing with an environment which could only store integers within the 32-bit signed integer range: [−231,  231 − 1]. If the numerical value is out of the range of representable values, INT_MAX (231 − 1) or INT_MIN (−231) is returned.
Example 1:

Input: "42"
Output: 42
Example 2:

Input: "   -42"
Output: -42
Explanation: The first non-whitespace character is '-', which is the minus sign.
             Then take as many numerical digits as possible, which gets 42.
Example 3:

Input: "4193 with words"
Output: 4193
Explanation: Conversion stops at digit '3' as the next character is not a numerical digit.
Example 4:

Input: "words and 987"
Output: 0
Explanation: The first non-whitespace character is 'w', which is not a numerical
             digit or a +/- sign. Therefore no valid conversion could be performed.
Example 5:

Input: "-91283472332"
Output: -2147483648
Explanation: The number "-91283472332" is out of the range of a 32-bit signed integer.
             Thefore INT_MIN (−231) is returned.
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
