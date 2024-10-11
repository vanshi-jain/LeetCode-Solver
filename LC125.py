import re
class Solution:
    def isPalindrome(self, s: str) -> bool:
        text = re.findall('[a-zA-Z0-9]', s)
        
        front = "".join(text).lower()
        back = front[::-1]
        
        return front == back
