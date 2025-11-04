class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        k = k%n #This ensures that even if k is larger you rotate with effective steps. So rotating 10 steps is the same as rotating 3 steps (because after every full cycle of 7, the array looks the same again)

        def reverse(l,r):
            while l<r:
                nums[l], nums[r] = nums[r], nums[l]
                l +=1
                r -=1
        
        reverse(0,n-1)
        reverse(0,k-1)
        reverse(k,n-1)
        