class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        charCount = {}
        freq = 0
        maxL = 0
        left = 0
        
        for right, let in enumerate(s):
            # get the char count from dict if exists and add one
            charCount[let] = charCount.get(let, 0) + 1
            # get the max freqeuncy of current char with prev freq
            freq = max(freq, charCount[let])

            while (right-left+1) - freq > k: # meaning this is invalid window if it exceeds k
                # shrink the window size from left
                charCount[s[left]] -= 1
                # increment the left pointer so reduce the widnow size
                left += 1
            
            # gte the max length from the running window
            maxL = max(maxL, right-left+1)
            
        return maxL
# The length of the current window is right - left + 1.
# We check if the current window can be made uniform by replacing up to k characters. 
# The formula (right - left + 1) - max_freq tells us how many characters in the window need to be 
# changed to match the most frequent character. If this value exceeds k, it means we can't make the window
#  valid with just k replacements.
# If the window is invalid, we "shrink" the window by moving the left pointer to the right 
# (increment left), and we reduce the frequency count of the character at the left boundary.
