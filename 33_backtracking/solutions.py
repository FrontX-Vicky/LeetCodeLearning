def permute(nums: list[int]) -> list[list[int]]:
    res = []
    
    def backtrack(curr_path, available):
        # Base case: if path is the same length as nums, we have a complete permutation
        if not available:
            res.append(curr_path[:]) # append a COPY of the path
            return
            
        for i in range(len(available)):
            # Choose
            curr_path.append(available[i])
            # Explore (pass available list WITHOUT the chosen element)
            backtrack(curr_path, available[:i] + available[i+1:])
            # Un-choose (backtrack)
            curr_path.pop()
            
    backtrack([], nums)
    return res

def combinationSum(candidates: list[int], target: int) -> list[list[int]]:
    res = []
    
    def backtrack(i, curr_path, current_sum):
        if current_sum == target:
            res.append(curr_path[:])
            return
        if i >= len(candidates) or current_sum > target:
            return
            
        # Decision 1: Include candidates[i] (can use it unlimited times)
        curr_path.append(candidates[i])
        backtrack(i, curr_path, current_sum + candidates[i])
        curr_path.pop()
        
        # Decision 2: Do NOT include candidates[i], move to next element
        backtrack(i + 1, curr_path, current_sum)
        
    backtrack(0, [], 0)
    return res
