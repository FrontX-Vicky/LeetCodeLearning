# Solutions.py - Reference Implementations
# These are complete, tested solutions for you to compare against

def daily_temperatures_brute(temperatures):
    """
    APPROACH 1: BRUTE FORCE (NESTED LOOPS)
    
    Concept: For each day, scan forward until we find a warmer temperature.
    
    Time: O(n²) - for each day, potentially scan all remaining days
    Space: O(1) - only output array
    """
    n = len(temperatures)
    result = [0] * n
    
    for i in range(n):
        # Scan forward from current day
        for j in range(i + 1, n):
            if temperatures[j] > temperatures[i]:
                result[i] = j - i
                break  # Found warmer day, stop scanning
        # If no warmer day found, result[i] stays 0
    
    return result


def daily_temperatures_stack(temperatures):
    """
    APPROACH 2: MONOTONIC DECREASING STACK
    
    Concept: Use stack to track indices of days waiting for warmer temperature.
    Stack maintains decreasing order of temperatures (monotonic property).
    
    When we encounter a warmer day:
    - It resolves all cooler days on the stack
    - Pop each cooler day and calculate wait time
    
    Time: O(n) - each index pushed and popped at most once
    Space: O(n) - stack can hold up to n indices
    """
    n = len(temperatures)
    result = [0] * n
    stack = []  # Stack stores indices in decreasing temperature order
    
    for i in range(n):
        # While current temp is warmer than stack top
        while stack and temperatures[i] > temperatures[stack[-1]]:
            prev_idx = stack.pop()
            result[prev_idx] = i - prev_idx
        
        # Push current index to stack (waiting for warmer day)
        stack.append(i)
    
    # Remaining indices in stack never found warmer day (already 0)
    return result


def daily_temperatures_stack_tuples(temperatures):
    """
    APPROACH 3: MONOTONIC STACK WITH TUPLES
    
    Concept: Same as Approach 2 but store (index, temperature) tuples
    for better code readability.
    
    Time: O(n)
    Space: O(n)
    """
    n = len(temperatures)
    result = [0] * n
    stack = []  # Stack stores (index, temperature) tuples
    
    for i, temp in enumerate(temperatures):
        # Pop all indices with cooler temperatures
        while stack and temp > stack[-1][1]:
            prev_idx, prev_temp = stack.pop()
            result[prev_idx] = i - prev_idx
        
        # Push current (index, temp) to stack
        stack.append((i, temp))
    
    return result


if __name__ == "__main__":
    print("Testing Approach 1: Brute Force")
    temps = [73, 74, 75, 71, 69, 72, 76, 73]
    print(f"  Input:  {temps}")
    print(f"  Output: {daily_temperatures_brute(temps)}")
    print(f"  Expected: [1, 1, 4, 2, 1, 1, 0, 0]")
    
    print("\nTesting Approach 2: Monotonic Stack")
    print(f"  Input:  {temps}")
    print(f"  Output: {daily_temperatures_stack(temps)}")
    print(f"  Expected: [1, 1, 4, 2, 1, 1, 0, 0]")
    
    print("\nTesting Approach 3: Stack with Tuples")
    print(f"  Input:  {temps}")
    print(f"  Output: {daily_temperatures_stack_tuples(temps)}")
    print(f"  Expected: [1, 1, 4, 2, 1, 1, 0, 0]")
    
    print("\n✓ All solutions working!")
