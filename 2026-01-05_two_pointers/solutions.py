# solutions.py - Reference solutions


def max_area_two_pointers(height):
    """
    Optimal: Two Pointers
    Time: O(n), Space: O(1)
    
    Algorithm:
    1. Start with pointers at both ends
    2. Calculate area with current pointers
    3. Move the pointer pointing to smaller height inward
    4. Track maximum area seen
    
    Why this works (greedy proof):
    - Area = width * min(left_height, right_height)
    - As we move pointers closer, width decreases
    - To increase area, we need height to increase more than width decreases
    - Moving the taller side can never give larger area (height won't increase enough)
    - Moving the shorter side might give larger area if new height is taller
    """
    if not height or len(height) < 2:
        return 0
    
    left = 0
    right = len(height) - 1
    max_area = 0
    
    while left < right:
        # Calculate area with current pointers
        width = right - left
        current_height = min(height[left], height[right])
        area = width * current_height
        max_area = max(max_area, area)
        
        # Move the pointer pointing to smaller height
        if height[left] < height[right]:
            left += 1
        else:
            right -= 1
    
    return max_area


def max_area_brute_force(height):
    """
    Baseline: O(n²) time, O(1) space
    """
    if not height or len(height) < 2:
        return 0
    
    max_area = 0
    
    for i in range(len(height)):
        for j in range(i + 1, len(height)):
            width = j - i
            current_height = min(height[i], height[j])
            area = width * current_height
            max_area = max(max_area, area)
    
    return max_area


def max_area_optimized(height):
    """
    Optimization: Two Pointers with pruning
    Time: O(n) with better average case
    Space: O(1)
    
    Improvement: If remaining width is too small to beat current max,
    we can skip checking some candidates
    """
    if not height or len(height) < 2:
        return 0
    
    left = 0
    right = len(height) - 1
    max_area = 0
    
    while left < right:
        # Early termination: if max possible area with remaining width
        # is less than current max, we can stop
        max_possible = (right - left) * max(height[left], height[right])
        if max_possible <= max_area:
            break
        
        width = right - left
        current_height = min(height[left], height[right])
        area = width * current_height
        max_area = max(max_area, area)
        
        # Move shorter side
        if height[left] < height[right]:
            left += 1
        else:
            right -= 1
    
    return max_area


# Which to use?
# Primary: max_area_two_pointers (clearest, optimal, no over-engineering)
# Alternative: max_area_optimized (if dealing with very large inputs with specific patterns)
