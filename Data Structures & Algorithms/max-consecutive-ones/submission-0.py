class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        count=0
        max_count = count
        for num in nums:
            if num==1: 
                count += 1
                if count > max_count : max_count = count
            else:
                count = 0
                continue
        
        return max_count

        