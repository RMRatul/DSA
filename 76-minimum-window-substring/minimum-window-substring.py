class Solution:
    def minWindow(self, s: str, t: str) -> str:
        need=[0]*128
        for i in t:
            need[ord(i)]+=1
        left=0
        right=0
        minLen=float('inf') 
        start=0
        count=len(t)

        while right<len(s):
            if (need[ord(s[right])]) >0:
                count-=1
            need[ord(s[right])]-=1
            right+=1

            while count==0:
                if right-left<minLen:
                    minLen=right-left
                    start=left
                need[ord(s[left])]+=1
                if (need[ord(s[left])]) >0:
                    count+=1
                left+=1
        if minLen==float('inf'): 
            return ""
        return s[start:start+minLen]
        