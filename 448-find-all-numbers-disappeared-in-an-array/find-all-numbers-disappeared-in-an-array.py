class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        n = len(nums)
        seen = [False] * (n + 1)

        for i in nums:
            seen[i] = True

        return [i for i in range(1, n+1) if not seen[i]]
        