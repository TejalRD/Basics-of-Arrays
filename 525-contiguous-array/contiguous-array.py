 #idea is to treat 0 as -1 and 1 as +1
class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        first_index = {0: -1}
        running = 0
        best =0

        for i,x in enumerate(nums):
            running += 1 if x ==1 else -1

            if running in first_index:
                best = max(best, i - first_index[running])
            else:
                first_index[running] = i

        return best


       
        