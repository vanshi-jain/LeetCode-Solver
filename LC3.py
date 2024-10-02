class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        sub = set()
        ans = 0
        l = 0
        for i in range(len(s)):
            while s[i] in sub: # found another occurence - repeated string
                sub.remove(s[l])
                l += 1
                # sub.clear()
                # sub.add(i)

            # after all ele are remvoed, add this ele
            sub.add(s[i])
            # check the ans - max of set with prev ans
            ans = max(ans, len(sub))
        

        return ans