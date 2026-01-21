# Main.py - Your Working File
# Task: Solve LeetCode #20: Valid Parentheses
# Goal: Write 3 progressive approaches using Stack

# TODO 1: Approach 1 - Stack with Dictionary Mapping
# - Create mapping: {')': '(', '}': '{', ']': '['}
# - For each char:
#   - If opening bracket → push to stack
#   - If closing bracket → pop and check if matches
# - Final check: stack should be empty
# - Time: O(n), Space: O(n)

def is_valid_stack_dict(s):
    """
    APPROACH 1: STACK WITH DICTIONARY MAPPING
    """
    if not s:
        return True
    
    closing_to_opening = {
        ")": "(",
        "}": "{",
        "]": "["
    }

    stack = []

    for char in s:
        if char in closing_to_opening:
            if not stack or stack[-1] != closing_to_opening[char]:
                return False
            stack.pop()
        else:
            stack.append(char)
    
    return len(stack) == 0        

# TODO 2: Approach 2 - Stack with Direct Comparison
# - Similar to Approach 1 but without dictionary
# - Use if-else chains to check matching
# - Slightly more memory efficient (no dict overhead)
# - Time: O(n), Space: O(n)

def is_valid_stack_direct(s):
    """
    APPROACH 2: STACK WITH DIRECT COMPARISON
    """
    if not s:
        return True
    
    stack = []

    for char in s:
        if char == '(' or char == '{' or char == '[':
            stack.append(char)
        else:
            if not stack:
                return False
            
            top = stack.pop()

            if char == ')' and top != '(':
                return False
            if char == '}' and top != '{':
                return False
            if char == ']' and top != '[':
                return False
    
    return len(stack) == 0

# TODO 3: Approach 3 - Stack with Early Returns (Optimized)
# - Check if length is odd → return False immediately
# - Return False as soon as mismatch detected
# - Better average case performance
# - Time: O(n), Space: O(n)

def is_valid_optimized(s):
    """
    APPROACH 3: STACK WITH EARLY RETURNS
    """
    if len(s) % 2 != 0:
        return False
    
    if not s:
        return True
    
    pairs = {')' : '(', '}' : '{', ']' : '['}
    stack = []

    for char in s:
        if char in pairs:
            if not stack or stack.pop() != pairs[char]:
                return False
        else:
            stack.append(char)
    
    return len(stack) == 0

if __name__ == "__main__":
    # Smoke tests
    # Test 1: Simple valid
    assert is_valid_stack_dict("()") == True
    assert is_valid_stack_direct("()") == True
    assert is_valid_optimized("()") == True
    
    # Test 2: Multiple types
    assert is_valid_stack_dict("()[]{}") == True
    assert is_valid_stack_direct("()[]{}") == True
    assert is_valid_optimized("()[]{}") == True
    
    # Test 3: Wrong type
    assert is_valid_stack_dict("(]") == False
    assert is_valid_stack_direct("(]") == False
    assert is_valid_optimized("(]") == False
    
    # Test 4: Wrong order
    assert is_valid_stack_dict("([)]") == False
    assert is_valid_stack_direct("([)]") == False
    assert is_valid_optimized("([)]") == False
    
    # Test 5: Valid nesting
    assert is_valid_stack_dict("{[]}") == True
    assert is_valid_stack_direct("{[]}") == True
    assert is_valid_optimized("{[]}") == True
    
    # Test 6: Only opening
    assert is_valid_stack_dict("(((") == False
    assert is_valid_stack_direct("(((") == False
    assert is_valid_optimized("(((") == False
    
    # Test 7: Only closing
    assert is_valid_stack_dict(")))") == False
    assert is_valid_stack_direct(")))") == False
    assert is_valid_optimized(")))") == False
    
    print("Quick checks passed. Run test_cases.py for more.")
