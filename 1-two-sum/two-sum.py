class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        lis ={}
        ans=[]
        for i,x in enumerate(nums):
            if x not in lis:
                lis[x] = i
            rem = target - x
            if rem in lis and lis[rem] != i:
                ans.append(lis[rem])
                ans.append(i)
                break

        
        return ans