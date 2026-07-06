class Solution:
    def findMin(self, nums: List[int]) -> int:
        l = 0
        r = len(nums) - 1
        ans = nums[0] # baseline

        while l <= r:
            if nums[l] < nums[r]: # sorted case
                ans = min(ans, nums[l])
                break
            mid = (l + r) // 2 # int division
            ans = min (ans, nums[mid])
            if nums[mid] >= nums[l]: # pivot must be in right, or on mid
                l = mid + 1
            else: # pivot must be left
                r = mid - 1

        return ans

        
