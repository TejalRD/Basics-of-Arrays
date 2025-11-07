class Solution:
    def beautifulArray(self, n: int) -> List[int]:
        arr = [1]
        while len(arr) <n:
            odds = [x*2-1 for x in arr if x*2-1 <=n]
            even = [x*2 for x in arr if x*2 <=n]
            arr = odds+even
        return arr
        