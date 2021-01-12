class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        l = len(nums)
        if l <= 1:
            return [nums]
        return [
            [i] + j for idx,i in enumerate(nums)
                    for j in self.permute(nums[:idx]+nums[idx+1:])
        ]
