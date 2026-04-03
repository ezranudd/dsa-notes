class Solution:

    # O(n)
    def productExceptSelf(self, nums: List[int]) -> List[int]:

        zeros = 0
        ret = [0] * len(nums)
        total = 1

        for num in nums:
            if num != 0:
                total *= num
            else:
                zeros += 1
        
        if zeros > 1:
            return ret
        
        if zeros == 1:
            for i in range(0,len(nums)):
                if nums[i] != 0:
                    ret[i] = 0
                else:
                    ret[i] = total 
            return ret

        for i in range(0,len(nums)):
            ret[i] = total // nums[i]
        return ret
