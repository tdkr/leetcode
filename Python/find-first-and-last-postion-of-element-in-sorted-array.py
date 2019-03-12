"""Find First and Last Position of Element in Sorted Array
https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array/

Given an array of integers nums sorted in ascending order, find the starting and ending position of a given target value.

Your algorithm's runtime complexity must be in the order of O(log n).

If the target is not found in the array, return [-1, -1].

Example 1:

Input: nums = [5,7,7,8,8,10], target = 8
Output: [3,4]
Example 2:

Input: nums = [5,7,7,8,8,10], target = 6
Output: [-1,-1]
"""

import json
import math

class Solution:
    def searchRange(self, nums: 'List[int]', target: int) -> 'List[int]':
        left, right = 0, len(nums)-1
        if left > right:
            return [-1, -1]
        
        mid = 0
        while left <= right:
            mid = math.floor((left+right)/2)
            if nums[mid] == target:
                break
            elif nums[mid] < target:
                left = mid+1
            else:
                right = mid-1
        
        if nums[mid] != target:
            return [-1, -1]
        
        left, right = 0, mid
        start = 0
        while left <= right:
            m = math.floor((left+right)/2)
            if nums[m] == target:
                right = m-1
                start = m
            else:
                left = m+1
                
        left, right = mid, len(nums)-1
        end = 0
        while left <= right:
            m = math.floor((left+right)/2)
            if nums[m] == target:
                left = m+1
                end = m
            else:
                right = m-1       
        # print(mid, start, end)
        return [start, end]

    def searchRange0(self, nums: 'List[int]', target: int) -> 'List[int]':
        left, right = 0, len(nums)-1
        if left > right:
            return [-1, -1]
        
        mid = 0
        while left <= right:
            mid = math.floor((left+right)/2)
            if nums[mid] == target:
                break
            elif nums[mid] < target:
                left = mid+1
            else:
                right = mid-1
        
        if nums[mid] != target:
            return [-1, -1]
        
        start = mid
        while start > 0 and nums[start-1] == nums[mid]:
            start -= 1
                
        end = mid
        while end < len(nums) - 1 and nums[end+1] == nums[mid]:
            end += 1
        # print(mid, start, end)
        return [start, end]


def stringToIntegerList(input):
    return json.loads(input)

def integerListToString(nums, len_of_list=None):
    if not len_of_list:
        len_of_list = len(nums)
    return json.dumps(nums[:len_of_list])

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
            
            ret = Solution().searchRange(nums, target)

            out = integerListToString(ret)
            print(out)
        except StopIteration:
            break

if __name__ == '__main__':
    main()