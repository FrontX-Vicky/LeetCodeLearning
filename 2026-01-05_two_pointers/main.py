# Main.py - Your Working File
# Task: Solve LeetCode #11: Container With Most Water
# Goal: Write 3 progressive approaches

# TODO 1: Approach 1 - Brute Force
# - Check all pairs of indices (i, j)
# - Calculate area for each pair: width * min(height[i], height[j])
# - Track maximum area
# - Time: O(n²), Space: O(1)

def max_area_brute_force(height):
    """
    APPROACH 1: BRUTE FORCE
    """
    #dont give suggetions for now
    area = 0 
    n = len(height)
    
    


# TODO 2: Approach 2 - Two Pointers (optimal)
# - Start with left pointer at start, right at end
# - Calculate area with current pointers
# - Move the pointer with smaller height inward (greedy)
# - Continue until pointers meet
# - Time: O(n), Space: O(1)
# - This is the standard interview solution

def max_area_two_pointers(height):
    """
    APPROACH 2: TWO POINTERS (OPTIMAL)
    """
    # YOUR CODE HERE
    pass


# TODO 3: Approach 3 - Two Pointers with early termination (optimization)
# - Same as Approach 2 but with early exit when width becomes negligible
# - Track minimum height seen to prune search space
# - Time: O(n) worst case, O(n) average (better pruning)

def max_area_optimized(height):
    """
    APPROACH 3: TWO POINTERS + OPTIMIZATION (REFERENCE)
    """
    # YOUR CODE HERE
    pass


if __name__ == "__main__":
    # Smoke tests
    assert max_area_two_pointers([1, 8, 6, 2, 5, 4, 8, 3, 7]) == 49
    assert max_area_two_pointers([1, 1]) == 1
    assert max_area_two_pointers([2, 3, 4, 5, 18, 17, 6]) == 17
    assert max_area_two_pointers([]) == 0
    assert max_area_two_pointers([1]) == 0
    print("Quick checks passed. Run test_cases.py for more.")
