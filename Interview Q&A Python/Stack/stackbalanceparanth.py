def is_balanced_parantheses(s):
    stack = []
    opening_brackets = ["(","{","["]
    closing_brackets = [")","}","]"]
    
    for char in s:
        if char in opening_brackets:
            stack.append(char)
        elif char in closing_brackets:
            if not stack or opening_brackets.index(stack.pop()) != closing_brackets.index(char):
                 return False
    return len(stack) == 0

# Test the function
string1 = "((()()()()))"
string2 = "((()()()())"

print(is_balanced_parantheses(string1))  # Output: True
print(is_balanced_parantheses(string2))  #Output: False
