class Solution:
    def minimumSum(self, num: int) -> int:
        list = sorted(str(num))
        return int(list[0] + list[2]) + int(list[1] + list[3])