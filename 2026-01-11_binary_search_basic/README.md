# Day 11: Binary Search - Basic Template

## LeetCode #704: Binary Search

### Problem Description
Given an array of integers `nums` which is sorted in **ascending order**, and an integer `target`, write a function to search `target` in `nums`. If `target` exists, then return its index. Otherwise, return `-1`.

You must write an algorithm with **O(log n)** runtime complexity.

**Example 1:**
```
Input: nums = [-1,0,3,5,9,12], target = 9
Output: 4
Explanation: 9 exists in nums and its index is 4
```

**Example 2:**
```
Input: nums = [-1,0,3,5,9,12], target = 2
Output: -1
Explanation: 2 does not exist in nums so return -1
```

**Constraints:**
- 1 ≤ nums.length ≤ 10⁴
- -10⁴ < nums[i], target < 10⁴
- All the integers in `nums` are **unique**
- `nums` is sorted in ascending order

---

## Three Approaches

### Approach 1: Iterative Binary Search (Classic)
**The standard template - master this!**

**Strategy:**
1. Use two pointers: `left = 0`, `right = len(nums) - 1`
2. While `left <= right`:
   - Calculate middle: `mid = (left + right) // 2`
   - If `nums[mid] == target`: return `mid`
   - If `nums[mid] < target`: search right half → `left = mid + 1`
   - If `nums[mid] > target`: search left half → `right = mid - 1`
3. If not found, return `-1`

**Why it works:**
- Each comparison eliminates half the search space
- Sorted array property: all left elements < mid, all right elements > mid

**Time Complexity:** O(log n) - halve search space each iteration
**Space Complexity:** O(1) - only use pointers

---

### Approach 2: Recursive Binary Search
**Elegant recursion approach**

**Strategy:**
1. Base case: `left > right` → return `-1` (not found)
2. Calculate `mid = (left + right) // 2`
3. If `nums[mid] == target`: return `mid`
4. If `nums[mid] < target`: recurse on right half `[mid+1, right]`
5. If `nums[mid] > target`: recurse on left half `[left, mid-1]`

**Why recursion works:**
- Each call solves a smaller subproblem
- Call stack handles the "backtracking" automatically

**Time Complexity:** O(log n) - log n recursive calls
**Space Complexity:** O(log n) - recursion call stack depth

---

### Approach 3: Alternative Mid Calculation (Avoids Overflow)
**Industry standard - prevents integer overflow**

**Strategy:**
- Use `mid = left + (right - left) // 2` instead of `(left + right) // 2`
- Rest of algorithm identical to Approach 1

**Why this matters:**
- In languages like Java/C++, `left + right` can overflow if both are large
- `left + (right - left) // 2` mathematically equivalent but safer
- Python integers don't overflow, but good practice for real interviews

**Time Complexity:** O(log n)
**Space Complexity:** O(1)

---

## Key Learnings

### 1. **Binary Search Template (Memorize This!)**
```python
def binary_search(nums, target):
    left, right = 0, len(nums) - 1
    
    while left <= right:  # NOTE: <= not <
        mid = left + (right - left) // 2
        
        if nums[mid] == target:
            return mid
        elif nums[mid] < target:
            left = mid + 1  # Search right
        else:
            right = mid - 1  # Search left
    
    return -1  # Not found
```

### 2. **Critical Details**
- **Condition:** `left <= right` (with `=`) because single element is valid
- **Update:** `left = mid + 1` and `right = mid - 1` (exclude mid, already checked)
- **Mid calculation:** `left + (right - left) // 2` prevents overflow

### 3. **When to Use Binary Search**
✅ Sorted array/list
✅ Search for specific value
✅ Need O(log n) time
❌ Unsorted data (sort first or use different approach)
❌ Need to find all occurrences (needs modification)

### 4. **Common Pitfalls**
- Using `left < right` instead of `left <= right` (misses single element)
- Forgetting to update `left = mid + 1` or `right = mid - 1` (infinite loop!)
- Wrong mid calculation: `(left + right) / 2` with `/` instead of `//`

---

## Testing Strategy

**Edge Cases:**
- Empty array (should handle gracefully)
- Single element (target found/not found)
- Target at boundaries (first/last element)
- Target not in array (return -1)
- Target in middle

**Test Coverage:**
- Various array sizes: 1, 2, 6, 10, 20 elements
- Target positions: start, middle, end, not present
- Negative numbers, zeros, positive numbers

---

## Real-World Applications

1. **Database indexing** - B-trees use binary search
2. **Version control** - `git bisect` finds buggy commits
3. **Dictionary lookups** - sorted dictionaries
4. **Game leaderboards** - find player rank
5. **Library systems** - ISBN search in sorted catalogs

---

## Master Concept: **Binary Search Paradigm**

**Core Principle:** 
Divide search space in half repeatedly → O(log n) efficiency

**Pattern Recognition:**
"Sorted" + "Find element" = Binary Search

**Interview Tip:**
Always ask: "Is the input sorted?" If yes, binary search likely optimal.

---

## Time to Practice! 🚀

Open `main.py` and implement all three approaches. Run `python test_cases.py` to verify!
