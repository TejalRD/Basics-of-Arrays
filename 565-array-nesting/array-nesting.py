class Solution:
    def arrayNesting(self, nums: List[int]) -> int:
        n = len(nums)
        longest = 0

        for i in range(n):
            if nums[i] == -1:
                continue
            count = 0
            j=i
            while nums[j] != -1:
                next = nums[j]
                nums[j] = -1
                j = next
                count += 1
            if count > longest:
                longest = count
        return longest

        