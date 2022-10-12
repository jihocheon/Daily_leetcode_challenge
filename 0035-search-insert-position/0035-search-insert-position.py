class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        lens = len(nums)
        for i,n in enumerate(nums):
            if(n >= target):
                return i
        return lens
        
            