from typing import List

class Solution:

    # O(n^2)
    def twoSumBruteForce(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                if nums[i] + nums[j] == target:
                    return [i,j]
        return [0,0]

    # Time: O(n)
    # Space: O(n)
    def twoSumHash(self, nums: List[int], target: int) -> List[int]:
        h = {}
        for i in range(len(nums)):
            if target - nums[i] in h:
                return [h[target - nums[i]], i]
            else:
                h[nums[i]] = i
        return [0,0]
