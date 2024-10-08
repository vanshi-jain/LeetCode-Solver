class Solution:
    def minWindow(self, s: str, t: str) -> str:
        left = 0
        res, resL = [-1,-1], float("inf")
        
        countT, window = {}, {}
        for c in t:
            countT[c] = countT.get(c, 0) + 1
        
        have, need = 0, len(countT)

        for right in range(len(s)):
            c = s[right]
            # first update the window count for this string
            window[c] = window.get(c, 0) + 1
            # second check if this string is what we need and compare the count
            if c in countT and window[c] == countT[c]:
                have += 1
            
            while have == need:
                # if conditions are met - we have what we need then update results
                if (right-left+1) < resL:
                    res = [left, right]
                    resL = (right-left+1)
                # pop from left window to shrink it
                window[s[left]] -= 1
                # but shrinking the window can cause a problem of losing needed char
                # if update window has less count that needed count for that char then we have one less char
                if s[left] in countT and window[s[left]] < countT[s[left]]:
                    have -= 1
                # increment the left pointer for reduced window size
                left += 1

        left, right = res
        return s[left:right+1] if resL != float("inf") else ""
