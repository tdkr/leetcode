"""Trapping Rain Water
https://leetcode.com/problems/trapping-rain-water/

Given n non-negative integers representing an elevation map where the width of each bar is 1, compute how much water it is able to trap after raining.

https://assets.leetcode.com/uploads/2018/10/22/rainwatertrap.png
The above elevation map is represented by array [0,1,0,2,1,0,1,3,2,1,2,1]. In this case, 6 units of rain water (blue section) are being trapped. Thanks Marcos for contributing this image!

Example:

Input: [0,1,0,2,1,0,1,3,2,1,2,1]
Output: 6
"""

import json

class Solution:
    def trap(self, height: 'List[int]') -> int:
        idx = 0
        start = height[idx]
        totalArea = 0
        curArea = 0
        while idx < len(height) - 1:
            idx += 1
            if height[idx] >= start:
                totalArea += curArea
                start = height[idx]
            else:
                curArea += start - height[idx]

        return totalArea

def stringToIntegerList(input):
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
            height = stringToIntegerList(line)
            
            ret = Solution().trap(height)

            out = str(ret)
            print(out)
        except StopIteration:
            break

if __name__ == '__main__':
    main()