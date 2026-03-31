from collections import defaultdict
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        myDict = defaultdict(int)
        for i,n in enumerate(nums):
        
            sub = target - n
            if sub in myDict:
                return [myDict[sub], i]
            myDict[n] = i

