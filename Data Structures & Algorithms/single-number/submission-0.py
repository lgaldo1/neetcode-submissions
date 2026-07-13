class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        # XORing identical numbers will become 0, which acts as a passthrough
        ans = 0
        for i in nums:
            ans = i ^ ans
        return ans
        