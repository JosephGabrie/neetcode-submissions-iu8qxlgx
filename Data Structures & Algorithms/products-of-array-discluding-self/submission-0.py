class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = []
        i = 0
        
        while i in range(len(nums)):
            num = 1
            j = 0
            while j in range(len(nums)):
                if j == i:
                    j += 1
                    continue
                num *= nums[j]
                j += 1
            res.append(num)
            i += 1
        return res
                

        