class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        return reduce(ixor, nums)