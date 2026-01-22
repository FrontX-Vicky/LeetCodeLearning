# Day 12: Binary Search Variations - First & Last Position

## LeetCode #34: Find First and Last Position of Element in Sorted Array

### Problem Description
Given an array of integers `nums` sorted in **non-decreasing order**, find the **starting and ending position** of a given `target` value.

If `target` is not found in the array, return `[-1, -1]`.

You must write an algorithm with **O(log n)** runtime complexity.

**Example 1:**
```
Input: nums = [5,7,7,8,8,10], target = 8
Output: [3,4]
Explanation: First occurrence at index 3, last at index 4
```

**Example 2:**
```
Input: nums = [5,7,7,8,8,10], target = 6
Output: [-1,-1]
Explanation: 6 is not in the array
```

**Example 3:**
```
Input: nums = [], target = 0
Output: [-1,-1]
```

**Constraints:**
- 0 ≤ nums.length ≤ 10⁵
- -10⁹ ≤ nums[i] ≤ 10⁹
- `nums` is a **non-decreasing** array (allows duplicates!)
- -10⁹ ≤ target ≤ 10⁹

---

## Three Approaches

### Approach 1: Two Binary Searches (Optimal)
**Find leftmost, then find rightmost**

**Strategy:**
1. **Find leftmost (first) occurrence:**
   - Use modified binary search
   - When `nums[mid] == target`, don't return immediately
   - Continue searching left: `right = mid - 1`
   - Track the last valid index found
   
2. **Find rightmost (last) occurrence:**
   - Use modified binary search
   - When `nums[mid] == target`, don't return immediately
   - Continue searching right: `left = mid + 1`
   - Track the last valid index found

**Why it works:**
- Standard binary search stops at ANY occurrence
- We need the FIRST and LAST occurrences
- By continuing to search even after finding target, we narrow to boundaries

**Time Complexity:** O(log n) - two binary searches
**Space Complexity:** O(1) - only use pointers

---

### Approach 2: Find One, Then Expand Linearly
**Quick but not optimal for interviews**

**Strategy:**
1. Use standard binary search to find ANY occurrence
2. If not found, return `[-1, -1]`
3. If found, expand left and right linearly to find boundaries

**Why it's suboptimal:**
- Binary search: O(log n)
- Expanding linearly: O(k) where k = count of target
- Worst case: entire array is target → O(n)
- Doesn't meet O(log n) requirement!

**Time Complexity:** O(n) worst case
**Space Complexity:** O(1)

---

### Approach 3: Single Pass with Python's bisect (Library Solution)
**Using Python's built-in binary search**

**Strategy:**
1. Use `bisect_left(nums, target)` → leftmost position to insert target
2. Use `bisect_right(nums, target)` → rightmost position to insert target
3. Validate indices and return

**Why it's elegant:**
- `bisect_left`: finds first occurrence index
- `bisect_right`: finds last occurrence index + 1
- One-liner solution with library support

**Time Complexity:** O(log n) - two bisect calls
**Space Complexity:** O(1)

**Note:** In interviews, implement Approach 1 manually. Bisect shows knowledge but may not satisfy "write the algorithm" requirement.

---

## Key Learnings

### 1. **Modified Binary Search Template (Find Leftmost)**
```python
def find_leftmost(nums, target):
    left, right = 0, len(nums) - 1
    result = -1
    
    while left <= right:
        mid = left + (right - left) // 2
        
        if nums[mid] == target:
            result = mid       # Save this position
            right = mid - 1    # Keep searching LEFT
        elif nums[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    
    return result
```

### 2. **Modified Binary Search Template (Find Rightmost)**
```python
def find_rightmost(nums, target):
    left, right = 0, len(nums) - 1
    result = -1
    
    while left <= right:
        mid = left + (right - left) // 2
        
        if nums[mid] == target:
            result = mid       # Save this position
            left = mid + 1     # Keep searching RIGHT
        elif nums[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    
    return result
```

### 3. **Key Differences from Standard Binary Search**
| Aspect | Standard | Find Leftmost | Find Rightmost |
|--------|----------|---------------|----------------|
| **When found** | Return immediately | Save, search left | Save, search right |
| **Goal** | Find any | Find first | Find last |
| **Direction** | Stop | Continue left | Continue right |

### 4. **Why We Need result Variable**
```
Array: [5, 7, 7, 7, 7, 10], target = 7

Finding leftmost:
  mid=2, nums[2]=7 → save result=2, search left
  mid=1, nums[1]=7 → save result=1, search left
  mid=0, nums[0]=5 → search right
  left > right → return result=1 ✓

Without result variable:
  Would return -1 (base case) → WRONG!
```

### 5. **When to Use This Pattern**
✅ Find first/last occurrence in sorted array
✅ Find range of values
✅ Count occurrences: `count = last - first + 1`
✅ Insert position in sorted array
❌ Unsorted arrays (need different approach)

---

## Testing Strategy

**Edge Cases:**
- Empty array
- Single element (found/not found)
- Target not in array
- All elements are target
- Target at boundaries (first/last position)
- Target appears once
- Target appears multiple times

**Test Coverage:**
- Various array sizes
- Different target positions
- Consecutive duplicates
- Negative numbers
- Large arrays

---

## Real-World Applications

1. **Database range queries** - find all records in date range
2. **Log analysis** - find all logs in time window
3. **Version control** - find commit range
4. **E-commerce** - find price range boundaries
5. **Time-series data** - find data in time span

---

## Master Concept: **Binary Search Boundary Finding**

**Core Principle:**
Don't stop when you find target - continue searching to find boundaries.

**Pattern Recognition:**
"Find first/last" + "Sorted array" = Modified Binary Search with boundary tracking

**Interview Tip:**
Always clarify: "Do you want ANY occurrence or FIRST/LAST occurrence?"
This determines whether to use standard or modified binary search.

---

## Time to Practice! 🚀

Open `main.py` and implement all three approaches. Run `python test_cases.py` to verify!
