class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        indices = {} # empty hash map
        
        for i, n in enumerate(nums): # (index, number)
            indices[n] = i;

        for i, n in enumerate(nums):
            remainder = target - n
            if remainder in indices and indices[remainder] != i:
                return [i, indices[remainder]]
        return []

        