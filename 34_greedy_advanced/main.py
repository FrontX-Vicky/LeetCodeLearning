def canJump(nums: list[int]) -> bool:
    """
    You are given an integer array nums. You are initially positioned at the array's first index,
    and each element in the array represents your maximum jump length at that position.
    Return true if you can reach the last index, or false otherwise.
    """
    max_reach = 0

    for i in range(len(nums)):
        if i > max_reach:
            return False
    
        max_reach = max(max_reach, i + nums[i])

        if max_reach >= len(nums) - 1:
            return True
    
    return True

        

def jump(nums: list[int]) -> int:
    """
    You are given a 0-indexed array of integers nums of length n. You are initially positioned at nums[0].
    Each element nums[i] represents the maximum length of a forward jump from index i. In other words,
    if you are at nums[i], you can jump to any nums[i + j] where:
    0 <= j <= nums[i] and i + j < n
    Return the minimum number of jumps to reach nums[n - 1].
    The test cases are generated such that you can reach nums[n - 1].
    """
    jumps = 0
    current_end = 0
    farthest = 0

    for i in range(len(nums) - 1):

        farthest = max(farthest, i + nums[i])

        if i == current_end:
            jumps += 1
            current_end = farthest

            if current_end >= len(nums) - 1:
                break
    
    return jumps

def main():
    print("Welcome to Day 34: Greedy Algorithms Advanced!")
    print("Run `python test_cases.py` to check your implementations.")

if __name__ == "__main__":
    main()
