# Solutions.py - Reference Implementations
# These are complete, tested solutions for you to compare against

def is_valid_stack_dict(s):
    """
    APPROACH 1: STACK WITH DICTIONARY MAPPING
    
    Concept: Use dictionary to map closing brackets to opening brackets.
    Stack tracks opening brackets. When we see closing bracket,
    verify it matches the most recent opening bracket.
    
    Time: O(n) - single pass through string
    Space: O(n) - stack can hold up to n/2 opening brackets
    """
    if not s:
        return True
    
    # Map closing brackets to their corresponding opening brackets
    closing_to_opening = {
        ')': '(',
        '}': '{',
        ']': '['
    }
    
    stack = []
    
    for char in s:
        if char in closing_to_opening:
            # It's a closing bracket
            # Check if stack is empty or top doesn't match
            if not stack or stack[-1] != closing_to_opening[char]:
                return False
            stack.pop()
        else:
            # It's an opening bracket
            stack.append(char)
    
    # Valid only if all brackets are matched (stack is empty)
    return len(stack) == 0


def is_valid_stack_direct(s):
    """
    APPROACH 2: STACK WITH DIRECT COMPARISON
    
    Same logic as Approach 1 but without dictionary.
    Directly compare characters using if-else chains.
    
    Time: O(n)
    Space: O(n)
    """
    if not s:
        return True
    
    stack = []
    
    for char in s:
        if char == '(' or char == '{' or char == '[':
            # Opening bracket - push to stack
            stack.append(char)
        else:
            # Closing bracket - check if stack has matching opening
            if not stack:
                return False
            
            top = stack.pop()
            
            # Check if the pair matches
            if char == ')' and top != '(':
                return False
            if char == '}' and top != '{':
                return False
            if char == ']' and top != '[':
                return False
    
    return len(stack) == 0


def is_valid_optimized(s):
    """
    APPROACH 3: STACK WITH EARLY RETURNS
    
    Optimizations:
    1. Check if length is odd - impossible to be valid
    2. Return False immediately on first mismatch
    3. Use dictionary for clean matching logic
    
    Time: O(n) worst case, better average case
    Space: O(n)
    """
    # Early return: odd length can never be valid
    if len(s) % 2 != 0:
        return False
    
    if not s:
        return True
    
    # Map closing to opening brackets
    pairs = {')': '(', '}': '{', ']': '['}
    stack = []
    
    for char in s:
        if char in pairs:
            # Closing bracket
            if not stack or stack.pop() != pairs[char]:
                return False  # Immediate return on mismatch
        else:
            # Opening bracket
            stack.append(char)
    
    return len(stack) == 0


if __name__ == "__main__":
    print("Testing Approach 1: Stack with Dictionary")
    print(f"  '()' → {is_valid_stack_dict('()')}")           # True
    print(f"  '()[]{{}}' → {is_valid_stack_dict('()[]{}')}") # True
    print(f"  '(]' → {is_valid_stack_dict('(]')}")           # False
    print(f"  '([)]' → {is_valid_stack_dict('([)]')}")       # False
    print(f"  '{{[]}}' → {is_valid_stack_dict('{[]}')}")     # True
    
    print("\nTesting Approach 2: Stack with Direct Comparison")
    print(f"  '()' → {is_valid_stack_direct('()')}")
    print(f"  '(]' → {is_valid_stack_direct('(]')}")
    print(f"  '{{[]}}' → {is_valid_stack_direct('{[]}')}")
    
    print("\nTesting Approach 3: Optimized with Early Returns")
    print(f"  '()' → {is_valid_optimized('()')}")
    print(f"  '((((((' → {is_valid_optimized('((((((')}")    # False (odd + unmatched)
    print(f"  '{{[]}}' → {is_valid_optimized('{[]}')}")
    
    print("\n✓ All solutions working!")
