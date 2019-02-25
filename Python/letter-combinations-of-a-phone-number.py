#!/usr/bin/env python3
"""Letter Combinations of a Phone Number
https://leetcode.com/problems/letter-combinations-of-a-phone-number/

Input: "23"
Output: ["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"].
"""

charMap = {
    "2":['a','b','c'],
    "3":['d','e','f'],
    "4":['g','h','i'],
    "5":['j','k','l'],
    "6":['m','n','o'],
    "7":['p','q','r','s'],
    "8":['t','u','v'],
    "9":['w','x','y','z'],
}

class Solution:
    def letterCombinations(self, digits: str) -> 'List[str]':
        total = []
        if len(digits) == 0:
            return total

        chars = charMap[digits[0]]
        if len(digits) == 1:
            return chars.copy()
            
        comb = self.letterCombinations(digits[1:])
        for i in chars:
            for j in comb:
                total.append(i + j)

        return total

print(Solution().letterCombinations("234"))