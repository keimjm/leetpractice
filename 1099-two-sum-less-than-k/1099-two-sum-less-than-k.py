class Solution:
    def twoSumLessThanK(self, nums: List[int], k: int) -> int:
        nums.sort()
        start, end = 0, len(nums) - 1
        possibleSum = -1
        while start < end:
            total = nums[start] + nums[end]
            if total < k:
                possibleSum = max(possibleSum, total)
                start += 1
            else:
                end -= 1
        return possibleSum