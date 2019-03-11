#!/usr/bin/env python3

"""Search in Rotated Sorted Array
https://leetcode.com/problems/search-in-rotated-sorted-array/

Suppose an array sorted in ascending order is rotated at some pivot unknown to you beforehand.

(i.e., [0,1,2,4,5,6,7] might become [4,5,6,7,0,1,2]).

You are given a target value to search. If found in the array return its index, otherwise return -1.

You may assume no duplicate exists in the array.

Your algorithm's runtime complexity must be in the order of O(log n).

Example 1:

Input: nums = [4,5,6,7,0,1,2], target = 0
Output: 4
Example 2:

Input: nums = [4,5,6,7,0,1,2], target = 3
Output: -1
"""

import math

class Solution:
    def searchRange(self, nums: 'List[int]', target: int, left: int, right: int) -> int:
        # print("searchRange", left, right)
        if target == nums[left]:
            return left
        elif target == nums[right]:
            return right
        elif left == right:
            return -1

        mid = math.floor((left + right)/2)
        if target == nums[mid]:
            return mid
        
        if target > nums[mid]:
            if target < nums[right]:
                return self.searchRange(nums, target, mid+1, right)
            elif nums[mid] >= nums[left]:
                return self.searchRange(nums, target, mid+1, right)
            else:
                return self.searchRange(nums, target, left, mid)
        else:
            if nums[mid] <= nums[right]:
                return self.searchRange(nums, target, left, mid)
            elif target > nums[left]:
                return self.searchRange(nums, target, left, mid)
            else:
                return self.searchRange(nums, target, mid+1, right)

    def search(self, nums: 'List[int]', target: int) -> int:
        if len(nums) == 0:
            return -1
        return self.searchRange(nums, target, 0, len(nums)-1)

def stringToIntegerList(input):
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
            nums = stringToIntegerList(line)
            line = next(lines)
            target = int(line)
            
            ret = Solution().search(nums, target)

            out = str(ret)
            print(out)
        except StopIteration:
            break

if __name__ == '__main__':
    main()