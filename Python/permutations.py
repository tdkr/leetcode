#!/usr/bin/env python3

"""Permutations
https://leetcode.com/problems/permutations/

Given a collection of distinct integers, return all possible permutations.

Example:

Input: [1,2,3]
Output:
[
  [1,2,3],
  [1,3,2],
  [2,1,3],
  [2,3,1],
  [3,1,2],
  [3,2,1]
]
"""

class Solution:
    def permute(self, nums: 'List[int]') -> 'List[List[int]]':
        if len(nums) <= 1:
            return [nums]
        
        total = []
        arr = self.permute(nums[1:])
        for v in arr:
            for i in range(0, len(v)+1):
                total.append(v[:i] + [nums[0]] + v[i:])
        # print("permute", nums, arr, total)
        return total

print(Solution().permute([1,2,3]))