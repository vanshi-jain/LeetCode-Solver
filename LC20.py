class Solution:
    def isValid(self, s: str) -> bool:
        bracks = {
            ')' : '(',
            '}' : '{',
            ']' : '['
        }
        stack = []
        for b in s:
            # opening brackets are stored in stack for further questioning
            if b in bracks.values():
                stack.append(b)
            # closing bracks or keys are checked against this stack
            elif b in bracks.keys():
                # if stack is not empty even after popping opening bracket
                # or the popped element is not equal to expected value
                # then game over
                if not stack or bracks[b] != stack.pop():
                    return False
            else:
                return False
        
        return (not stack)
        
