class Solution(object):
    def minEatingSpeed(self, piles, h):
        """
        :type piles: List[int]
        :type h: int
        :rtype: int
        """
        left,right= 1,max(piles)
        res = right
        while(left<=right):
            totalTime=0
            mid = (left+right)//2
            for p in piles:
                totalTime+=math.ceil(float(p)/mid)
            if totalTime<=h:
                right = mid-1
                res=mid
            else:
                left=mid+1
        return res