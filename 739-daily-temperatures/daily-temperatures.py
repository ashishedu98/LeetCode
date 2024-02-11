class Solution(object):
    def dailyTemperatures(self, temp):
        """
        :type temperatures: List[int]
        :rtype: List[int]
        """
        stack = []
        ans = [None] * len(temp)
        for i,x in enumerate(temp):
            if(i==0):
                stack.append((x,i))
                continue
            while(stack and x>stack[-1][0]):
                y = stack[-1]
                stack.pop()
                ans[y[1]] = i- y[1]
            stack.append((x,i))
        while(stack):
            y = stack.pop()
            ans[y[1]] = 0
            
        return ans

