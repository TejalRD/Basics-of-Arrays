class Solution:
    def arrayPairSum(self, nums: List[int]) -> int:
        #sort the array and pair adjacent numbers, then answer will simply be the sum of elements at even indices.
        nums.sort()
        return sum(nums[::2])


        