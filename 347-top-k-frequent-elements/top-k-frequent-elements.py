from typing import List

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        n = len(nums)

        # Step 1: Count frequency
        freq = {}

        for num in nums:
            freq[num] = freq.get(num, 0) + 1

        # Step 2: Create buckets
        # buckets[i] = numbers that appear exactly i times
        buckets = [[] for _ in range(n + 1)]

        for num, count in freq.items():
            buckets[count].append(num)

        # Step 3: Traverse from highest frequency
        result = []

        for i in range(n, 0, -1):
            for num in buckets[i]:
                result.append(num)

                if len(result) == k:
                    return result

        
        