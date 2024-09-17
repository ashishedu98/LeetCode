class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        ans =[]
        intervals.sort()

        prev = intervals[0]
        for x in intervals[1:]:
            if x[0] <= prev[1]:
                prev[1] = max(prev[1], x[1])
            else:
                ans.append(prev)
                prev = x
        ans.append(prev)
        return ans