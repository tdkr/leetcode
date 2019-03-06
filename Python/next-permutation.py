import json

class Solution:
    def nextPermutation(self, nums: 'list[int]') -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        if nums == None or len(nums) < 2:
            return
        for i in range(len(nums)-2, -1, -1):
            value = nums[i]
            for j in range(len(nums)-1, i, -1):
                if value < nums[j]:
                    v = nums.pop(j)
                    nums.insert(i, v)
                    nums[i+1:] = sorted(nums[i+1:])
                    return
        return list.sort(nums)
        


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
            
            ret = Solution().nextPermutation(nums)

            out = integerListToString(nums)
            if ret is not None:
                print("Do not return anything, modify nums in-place instead.")
            else:
                print(out)
        except StopIteration:
            break

if __name__ == '__main__':
    main()