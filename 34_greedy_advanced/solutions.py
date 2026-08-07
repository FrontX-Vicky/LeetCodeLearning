def canJump(nums: list[int]) -> bool:
    # We want to keep track of the maximum index we can reach.
    max_reach = 0
    
    for i in range(len(nums)):
        # If the current index is greater than our maximum reach, we're stuck
        if i > max_reach:
            return False
            
        # Update maximum reach
        max_reach = max(max_reach, i + nums[i])
        
        # Early exit if we can already reach the end
        if max_reach >= len(nums) - 1:
            return True
            
    return True

def jump(nums: list[int]) -> int:
    # Number of jumps made so far
    jumps = 0
    
    # The maximum index we can reach with the current number of jumps
    current_end = 0
    
    # The maximum index we can reach with (jumps + 1) jumps
    farthest = 0
    
    # We loop up to len(nums) - 1 because we don't need to jump from the last index
    for i in range(len(nums) - 1):
        # Update the farthest index reachable from here
        farthest = max(farthest, i + nums[i])
        
        # If we have reached the end of the range for our current jump
        if i == current_end:
            jumps += 1
            current_end = farthest
            
            # Optimization: If we can reach the end, stop early
            if current_end >= len(nums) - 1:
                break
                
    return jumps
