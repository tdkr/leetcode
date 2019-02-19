#!/usr/bin/env python3

"""Container With Most Water
https://leetcode.com/problems/container-with-most-water/
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