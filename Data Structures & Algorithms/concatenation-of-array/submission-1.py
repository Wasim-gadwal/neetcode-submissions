class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        n = len(nums)
        ans = [0] * 2 * n
        for idx, val in enumerate(ans):
            if idx < n:
                ans[idx] = nums[idx]
            else:
                ans[idx] = nums[idx - n]
        return ans

