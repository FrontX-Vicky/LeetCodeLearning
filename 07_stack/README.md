# Day 7: Stack - Valid Parentheses

**Date:** January 17, 2026  
**Topic:** Stack Data Structure (LIFO - Last In First Out)  
**Problem:** LeetCode #20 - Valid Parentheses  
**Difficulty:** Easy

---

## Problem Statement

Given a string `s` containing just the characters `'('`, `')'`, `'{'`, `'}'`, `'['` and `']'`, determine if the input string is valid.

An input string is valid if:
1. Open brackets must be closed by the same type of brackets.
2. Open brackets must be closed in the correct order.
3. Every close bracket has a corresponding open bracket of the same type.

### Example 1:
```
Input: s = "()"
Output: true
```

### Example 2:
```
Input: s = "()[]{}"
Output: true
```

### Example 3:
```
Input: s = "(]"
Output: false
Explanation: Opening '(' doesn't match closing ']'
```

### Example 4:
```
Input: s = "([)]"
Output: false
Explanation: Wrong order - '[' is opened last but ']' closes before ')'
```

### Example 5:
```
Input: s = "{[]}"
Output: true
Explanation: Correct nesting
```

### Constraints:
- `1 <= s.length <= 10^4`
- `s` consists of parentheses only `'()[]{}'`

---

## Approach 1: Stack with Dictionary Mapping

**Concept:** Use a stack to track opening brackets. When we see a closing bracket, check if it matches the most recent opening bracket.

**Algorithm:**
1. Create a stack (list in Python)
2. Create a mapping: `{')': '(', '}': '{', ']': '['}`
3. For each character:
   - If opening bracket `(`, `{`, `[` → push to stack
   - If closing bracket `)`, `}`, `]`:
     - If stack is empty → invalid (no matching opener)
     - Pop from stack and check if it matches
4. After processing all chars, stack should be empty

**Why Stack?**
- Last opened bracket must be first closed (LIFO behavior)
- Perfect match for nested structures

**Complexity:**
- Time: O(n) - single pass through string
- Space: O(n) - worst case all opening brackets

**Pros:** Clean and intuitive  
**Cons:** Uses extra space for mapping dict

---

## Approach 2: Stack with Direct Comparison

**Concept:** Similar to Approach 1 but without dictionary - directly compare characters.

**Algorithm:**
1. For each character:
   - If opening `(`, `{`, `[` → push to stack
   - If closing `)`, `}`, `]`:
     - Check if stack is empty (invalid)
     - Pop and verify match using if-else
2. Return `len(stack) == 0`

**Complexity:**
- Time: O(n)
- Space: O(n) for stack only (no extra dict)

**Pros:** Slightly more memory efficient  
**Cons:** More verbose matching logic

---

## Approach 3: Stack with Early Returns

**Concept:** Optimize by returning early on obvious failures.

**Algorithm:**
1. Check length: if odd, return False immediately (can't pair)
2. Use stack with early exit conditions
3. Return as soon as we detect mismatch

**Optimization:**
- Odd length strings are always invalid
- Return False immediately on mismatch (don't wait till end)
- Reduces unnecessary iterations

**Complexity:**
- Time: O(n) worst case, better average case
- Space: O(n)

**Pros:** Faster average performance  
**Cons:** Similar worst-case complexity

---

## Key Learnings

1. **Stack = LIFO (Last In, First Out):** Perfect for nested/paired structures
2. **Common Stack Uses:**
   - Parentheses matching
   - Expression evaluation
   - Backtracking problems
   - Undo/redo functionality
   - Browser history
3. **Dictionary Mapping:** Clean way to define pairs/relationships
4. **Early Returns:** Optimize by failing fast on impossible cases

---

## Stack Fundamentals

### What is a Stack?
```
     │   5   │  ← Top (last added, first removed)
     ├───────┤
     │   3   │
     ├───────┤
     │   1   │
     └───────┘  ← Bottom
```

### Operations:
- **Push:** Add to top - O(1)
- **Pop:** Remove from top - O(1)
- **Peek/Top:** View top without removing - O(1)
- **isEmpty:** Check if empty - O(1)

### In Python:
```python
stack = []           # Create empty stack
stack.append(5)      # Push
top = stack[-1]      # Peek
value = stack.pop()  # Pop
is_empty = len(stack) == 0
```

---

## Common Mistakes

1. **Not checking empty stack before pop:**
   ```python
   # ❌ WRONG
   if stack.pop() != expected:
       return False  # Crashes if stack is empty!
   
   # ✅ CORRECT
   if not stack or stack.pop() != expected:
       return False
   ```

2. **Forgetting to check final stack state:**
   ```python
   # ❌ WRONG
   # Process all chars...
   return True  # What if stack still has unpaired opening brackets?
   
   # ✅ CORRECT
   return len(stack) == 0
   ```

3. **Wrong matching logic:**
   ```python
   # ❌ WRONG
   if char == ')' and stack.pop() == ')':  # Comparing closing to closing!
   
   # ✅ CORRECT
   if char == ')' and stack.pop() == '(':  # Opening matches closing
   ```

4. **Not handling odd-length strings:**
   ```python
   # Missing optimization
   if len(s) % 2 != 0:
       return False  # Odd length can never be valid
   ```

---

## Visual Trace Example

**Input:** `s = "{[()]}"`

```
Step  Char  Stack State      Action
────────────────────────────────────────
0     {     ['{']           Push opening
1     [     ['{', '[']      Push opening
2     (     ['{', '[', '('] Push opening
3     )     ['{', '[']      Pop '(' - matches ')'  ✓
4     ]     ['{']           Pop '[' - matches ']'  ✓
5     }     []              Pop '{' - matches '}'  ✓
End         Empty stack     Valid! Return True
```

**Input:** `s = "([)]"`

```
Step  Char  Stack State      Action
────────────────────────────────────────
0     (     ['(']           Push opening
1     [     ['(', '[']      Push opening
2     )     ['(']           Pop '[' - WRONG! ✗
                            '[' doesn't match ')'
                            Return False
```

---

## Follow-up Variations

- **LeetCode #921:** Minimum Add to Make Parentheses Valid
- **LeetCode #1021:** Remove Outermost Parentheses
- **LeetCode #1190:** Reverse Substrings Between Each Pair of Parentheses
- **LeetCode #32:** Longest Valid Parentheses (Hard)

---

## When to Use Stack Pattern?

✅ **Use Stack When:**
- Matching/pairing elements (parentheses, tags)
- Reversing order
- Backtracking (undo operations)
- Nested structures
- Expression evaluation
- Depth-first traversal

❌ **Don't Use Stack When:**
- Need random access (use array/list)
- Need to maintain sorted order (use heap)
- Need first-in-first-out (use queue)
