class Solution:
    def isValid(self, s):
        # Check if the string length is odd
        if len(s) % 2 != 0:
            return False
        
        # Mapping of closing brackets to their corresponding opening brackets
        bracket_map = {')': '(', '}': '{', ']': '['}
        stack = []
        
        for char in s:
            # If the character is a closing bracket
            if char in bracket_map:
                # Check if the stack is empty or the top of the stack doesn't match
                if not stack or stack[-1] != bracket_map[char]:
                    return False
                stack.pop()  # Pop the matched opening bracket
            else:
                # If it's an opening bracket, push onto the stack
                stack.append(char)
        
        # Return True if stack is empty, meaning all brackets were matched
        return not stack