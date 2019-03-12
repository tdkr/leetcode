"""
39.Combination Sum
https://leetcode.com/problems/combination-sum/

Given a set of candidate numbers (candidates) (without duplicates) and a target number (target), find all unique combinations in candidates where the candidate numbers sums to target.

The same repeated number may be chosen from candidates unlimited number of times.

Note:

All numbers (including target) will be positive integers.
The solution set must not contain duplicate combinations.
Example 1:

Input: candidates = [2,3,6,7], target = 7,
A solution set is:
[
  [7],
  [2,2,3]
]
Example 2:

Input: candidates = [2,3,5], target = 8,
A solution set is:
[
  [2,2,2,2],
  [2,3,3],
  [3,5]
]
"""

class Solution:    
    def combinationSum(self, candidates: 'List[int]', target: int) -> 'List[List[int]]':
        total = []
        candidates.sort()
        def dfs(left: int, path: 'List[int]', idx: int):
            if left == 0:
                total.append(path[:])
                return
            for i, v in enumerate(candidates[idx:]):
                if v > left:
                    break
                dfs(left-v, path + [v], idx+i)

        dfs(target, [], 0)
        return total

    def findCombs(self, candidates: 'List[int]', target: int, dp: 'map[int]') -> 'List[List[int]]':
        if target in dp:
            return dp[target]
        total = []
        dp[target] = total
        mark = {}
        for v in candidates:
            if target < v:
                continue
            if target == v:
                total.append([v])
                continue
            arr = self.findCombs(candidates, target-v, dp)     
            for k in arr:
                t = [v] + k
                t.sort()
                key = ''.join(str(e) for e in t)
                if key not in mark:
                    total.append(t)
                    mark[key] = True
        # print("findCombs", target, candidates, total)
        return total

    def combinationSum0(self, candidates: 'List[int]', target: int) -> 'List[List[int]]':
        dp = {}
        return self.findCombs(candidates, target, dp)

print(Solution().combinationSum([2,3,5], 8))
print(Solution().combinationSum([2,3,6,7], 7))