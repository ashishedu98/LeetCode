class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        ans=[]
        for x in nums:
            count[x] = 1 + count.get(x,0)

        print(count)
        sorted_count = dict(sorted(count.items(), key=lambda x:x[1], reverse =True))
        print(sorted_count)

        for item in sorted_count:
            if k>0:
                ans.append(item)
                k-=1
            else: break

        return ans

        