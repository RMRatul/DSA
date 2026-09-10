class Solution:
    def dailyTemperatures(self, temperatures: list[int]) -> list[int]:

       ans = [0] * len(temperatures) 
       stack=[]

       for right in range(len(temperatures)):
        while stack and temperatures[right]>temperatures[stack[-1]]:
          left=stack.pop()
          ans[left]=right-left
        stack.append(right)

       return ans