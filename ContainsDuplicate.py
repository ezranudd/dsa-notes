from typing import List

class Solution:

    # Brute Force Method
    # Time: O(n^2)
    # Space: O(1)
    def hasDuplicateBruteForce(self, nums: List[int]) -> bool:
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                if nums[i] == nums[j]:
                    return True
        return False

    # Array Sort Method
    # Time: O(n log n)
    # Space: O(1) extra (in-place sort), though Python's Timsort uses auxiliary memory internally
    def hasDuplicateSort(self, nums: List[int]) -> bool:
        nums.sort()
        for i in range(1, len(nums)):
            if nums[i] == nums[i - 1]:
                return True
        return False

    # HashSet Method (Optimal)
    # Time: O(n)
    # Space: O(n)
    def hasDuplicateHashSet(self, nums: List[int]) -> bool:
        hashset = set()
        for n in nums:
            if n in hashset:
                return True
            hashset.add(n)
        return False