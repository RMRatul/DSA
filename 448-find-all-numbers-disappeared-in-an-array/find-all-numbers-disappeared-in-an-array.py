class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        for i in nums:
            val=abs(i)-1
            nums[val]=-1*abs(nums[val])
        res=[]
        for i,n in enumerate(nums):
            if n>0:
                res.append(i+1)
        return res
        