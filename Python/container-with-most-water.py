#!/usr/bin/env python3

"""Container With Most Water
https://leetcode.com/problems/container-with-most-water/

Given n non-negative integers a1, a2, ..., an , where each represents a point at coordinate (i, ai). n vertical lines are drawn such that the two endpoints of line i is at (i, ai) and (i, 0). Find two lines, which together with x-axis forms a container, such that the container contains the most water.

Note: You may not slant the container and n is at least 2.

https://s3-lc-upload.s3.amazonaws.com/uploads/2018/07/17/question_11.jpg

The above vertical lines are represented by array [1,8,6,2,5,4,8,3,7]. In this case, the max area of water (blue section) the container can contain is 49. 

Example:

Input: [1,8,6,2,5,4,8,3,7]
Output: 49

ref:
最简单遍历所有组合得出最大值
优化:
用两个指针记录左右位置，移动遵守以下规则：
左边低则往右移，右边低则往左移
"""

class Solution:
    def calArea(self, height, left, right):
        width = right - left
        height = height[left] if height[left] < height[right] else height[right]
        return width * height

    def maxArea(self, height: []):
        max_area = 0
        left, right = 0, len(height) - 1
        while left < right:
            area = self.calArea(height, left, right)
            if area > max_area:
                max_area = area

            if height[left] <= height[right]:
                left = left + 1
            else:
                right = right - 1
        return max_area

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
            height = stringToIntegerList(line)
            
            ret = Solution().maxArea(height)

            out = str(ret)
            print(out)
        except StopIteration:
            break

if __name__ == '__main__':
    main()