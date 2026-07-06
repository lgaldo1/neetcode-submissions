class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l = 0
        r = len(nums) - 1

        while l <= r:
            mid = (l + r) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] >= nums[l]: # if left sorted, pivot is on right
                if (target > nums[mid] or target < nums[l]): # oob for left
                    l = mid + 1
                else:
                    r = mid - 1
            else: # pivot is on left, right is sorted
                if (target < nums[mid] or target > nums[r]): # oob for right
                    r = mid - 1
                else:
                    l = mid + 1



        return -1