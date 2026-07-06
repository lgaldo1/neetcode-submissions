class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        match = {")" : "(", "}" : "{","]" : "["} 
        # close is a key for the opening

        for char in s:
            if char in match: # closing
                if stack and stack[-1] == match[char]: # making sure not empty
                    stack.pop()
                else: # empty or mismatch
                    return False
            else: # opening
                stack.append(char)
        
        return (not stack)
        