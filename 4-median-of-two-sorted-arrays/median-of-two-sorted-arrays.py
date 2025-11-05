class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        a,b = nums1, nums2
        m,n = len(a), len(b)

        #ensure a is the smaller array
        if m>n:
            a,b,m,n = b,a,n,m

        total = m+n
        half = (total +1) //2

        lo,hi = 0,m
        while lo <= hi:
            i= (lo +hi)//2  #cut in a
            j= half-i       #cut in b

            aleft = a[i-1] if i>0 else float("-inf")
            aright = a[i] if i<m else float("inf")
            bleft = b[j-1] if j>0 else float("-inf")
            bright = b[j] if j<n else float("inf")

            if aleft <= bright and bleft <=aright:
                if total %2:
                    return float(max(aleft,bleft))
                return(max(aleft,bleft)+min(aright,bright))/2.0
            elif aleft>bright:
                    hi = i-1
            else:
                    lo = i+1



        