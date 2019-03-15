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
        area = 0
        left, right = 0, len(height)-1
        while True:
            # print(left, right, area)

            # 忽略左边更小的柱子
            while left < len(height)-1 and height[left] < height[left+1]:
                left += 1
            
            # 忽略右边更小的柱子
            while right > 0 and height[right] < height[right-1]:
                right -= 1

            if left >= right:
                break

            # 如果左边柱子比右边柱子低，则从左边开始往右遍历直到更高的柱子出现
            # 反之亦然
            if height[left] <= height[right]:
                idx = left + 1
                while idx < right and height[left] > height[idx]:
                    area += height[left] - height[idx]
                    idx += 1
                left = idx
            else:
                idx = right - 1
                while idx > left and height[right] > height[idx]:
                    area += height[right] - height[idx]
                    idx -= 1
                right = idx
        return area

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