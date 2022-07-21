class Solution:
    def rob(self, nums: List[int]) -> int:
        # decision = [(nums[0] + nums[2:]), (nums[1] + nums[3:])]
        rob1, rob2 = 0, 0
        
        for n in nums:
            temp = max(rob1 + n, rob2)
            rob1 = rob2
            rob2 = temp
        return rob2