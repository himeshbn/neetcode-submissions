class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        matching_char = { ')':'(', '}':'{', ']':'['}

        for char in s:
            if char in matching_char:
                top_element =  stack.pop() if stack else '#'

                if matching_char[char] != top_element:
                    return False
            else:
                stack.append(char)
        
        return not stack
        

        