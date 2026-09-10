class Solution:
    def findAnagrams(self, s: str, p: str):
        if len(p) > len(s):
            return []

        result = []

       
        p_count = {}

        for char in p:
            p_count[char] = p_count.get(char, 0) + 1
        
        window_count = {}
        left = 0
        
        for right in range(len(s)):
          window_count[s[right]] = window_count.get(s[right], 0) + 1
          
          
          if right - left + 1 > len(p):
            
            window_count[s[left]] -= 1
            
            if window_count[s[left]] == 0:
              del window_count[s[left]]
            
            left += 1
          
         
          if right - left + 1 == len(p) and window_count == p_count:
            result.append(left)

        return result



