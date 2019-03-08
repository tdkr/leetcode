"""Longest Valid Parentheses
https://leetcode.com/problems/longest-valid-parentheses/

Given a string containing just the characters '(' and ')', find the length of the longest valid (well-formed) parentheses substring.

Example 1:

Input: "(()"
Output: 2
Explanation: The longest valid parentheses substring is "()"
Example 2:

Input: ")()())"
Output: 4
Explanation: The longest valid parentheses substring is "()()"
"""
class Solution:
    def longestValidParentheses(self, s: str) -> int:
        maxLen = 0
        right, left = -1, 0
        dp = {}
        for i in range(1, len(s)):
            if s[i] == ")":
                if s[i-1] == "(":
                    left, right = i-1, i
                elif s[i-1] == ")" and right == i-1 and left > 0 and s[left-1] == "(":
                    left, right = left-1, i     
                else:
                    continue           
                if left-1 in dp:
                    left = dp[left-1]
                dp[right] = left
                length = right - left + 1
                if length > maxLen:
                    maxLen = length
        return maxLen

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
            
            ret = Solution().longestValidParentheses(s)

            out = str(ret)
            print(out)
        except StopIteration:
            break

if __name__ == '__main__':
    main()