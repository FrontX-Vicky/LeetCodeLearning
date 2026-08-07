def permute(nums: list[int]) -> list[list[int]]:
    """
    Given an array nums of distinct integers, return all the possible permutations.
    You can return the answer in any order.
    """
    res = []

    def backtrack(curr_path, available):
        if not available:
            res.append(curr_path[:])
            return
        
        for i in range(len(available)):
            curr_path.append(available[i])

            backtrack(curr_path, available[:i] + available[i+1:])

            curr_path.pop()

    backtrack([], nums)
    return res

def combinationSum(candidates: list[int], target: int) -> list[list[int]]:
    """
    Given an array of distinct integers candidates and a target integer target,
    return a list of all unique combinations of candidates where the chosen numbers sum to target.
    You may return the combinations in any order.
    The same number may be chosen from candidates an unlimited number of times.
    """
    res = []

    def backtrack(i, curr_path, current_sum):
        if current_sum == target:
            res.append(curr_path[:])
            return
        if i >= len(candidates) or current_sum > target:
            return 
        
        curr_path.append(candidates[i])
        backtrack(i, curr_path, current_sum + candidates[i])
        curr_path.pop()

        backtrack(i + 1, curr_path, current_sum)
    
    backtrack(0, [], 0)
    return res

def main():
    print("Welcome to Day 33: Backtracking (Combinations/Permutations)!")
    print("Run `python test_cases.py` to check your implementations.")

if __name__ == "__main__":
    main()
