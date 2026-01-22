# Main.py - Your Working File
# Task: Solve LeetCode #739: Daily Temperatures
# Goal: Find days until warmer temperature using Monotonic Stack

# TODO 1: Approach 1 - Brute Force (Nested Loops)
# - For each day, scan forward to find next warmer day
# - Simple but O(n²) time complexity
# - Time: O(n²), Space: O(1)

def daily_temperatures_brute(temperatures):
    """
    APPROACH 1: BRUTE FORCE
    """
    result = []
    for i, t in enumerate(temperatures):
        d = 0
        u = True
        for j in temperatures[i + 1:]:
            d += 1
            if j > t:
                u = False
                result.append(d)
                break
        if u:
            result.append(0)

    return result


# TODO 2: Approach 2 - Monotonic Decreasing Stack
# - Use stack to store indices of days waiting for warmer temp
# - Stack maintains decreasing order of temperatures
# - When warmer day found, pop and calculate wait time
# - Time: O(n), Space: O(n)

def daily_temperatures_stack(temperatures):
    """
    APPROACH 2: MONOTONIC DECREASING STACK
    """
    n = len(temperatures)
    result = [0] * n
    stack = [] # stack stores indices in decreasing teprature order

    for i in range(n):
        # while current temp is warmer then stack top
        while stack and temperatures[i] > temperatures[stack[-1]]:
            prev_idx = stack.pop()
            result[prev_idx] = i - prev_idx

        # push current index to stack (waiting for warmer day)
        stack.append(i)
    
    return result


# TODO 3: Approach 3 - Monotonic Stack with Tuples
# - Store (index, temperature) tuples for clarity
# - Same algorithm as Approach 2 but more readable
# - Time: O(n), Space: O(n)

def daily_temperatures_stack_tuples(temperatures):
    """
    APPROACH 3: MONOTONIC STACK WITH TUPLES
    """
    n = len(temperatures)
    result = [0] * n
    stack = [] # stack stores index temprature tuples

    for i, temp in enumerate(temperatures):
        # pop all indices with cooler temperature
        while stack and temp > stack[-1][1]:
            prev_idx, prev_temp = stack.pop()
            result[prev_idx] = i - prev_idx
        
        # push current (index, temp) to stack
        stack.append((i, temp))
    
    return result




if __name__ == "__main__":
    # Smoke tests
    
    # Test 1: Example from problem
    temps1 = [73, 74, 75, 71, 69, 72, 76, 73]
    expected1 = [1, 1, 4, 2, 1, 1, 0, 0]
    
    print("Testing Approach 1: Brute Force")
    result1 = daily_temperatures_brute(temps1)
    assert result1 == expected1, f"Expected {expected1}, got {result1}"
    print(f"  {temps1}")
    print(f"  -> {result1}")
    print("  ✓ Passed!")
    
    exit()
    print("\nTesting Approach 2: Monotonic Stack")
    result2 = daily_temperatures_stack(temps1)
    assert result2 == expected1, f"Expected {expected1}, got {result2}"
    print(f"  {temps1}")
    print(f"  -> {result2}")
    print("  ✓ Passed!")
    
    print("\nTesting Approach 3: Stack with Tuples")
    result3 = daily_temperatures_stack_tuples(temps1)
    assert result3 == expected1, f"Expected {expected1}, got {result3}"
    print(f"  {temps1}")
    print(f"  -> {result3}")
    print("  ✓ Passed!")
    
    # Test 2: Increasing sequence
    temps2 = [30, 40, 50, 60]
    expected2 = [1, 1, 1, 0]
    
    assert daily_temperatures_brute(temps2) == expected2
    assert daily_temperatures_stack(temps2) == expected2
    assert daily_temperatures_stack_tuples(temps2) == expected2
    
    print("\nAll smoke tests passed! Run test_cases.py for comprehensive tests.")
