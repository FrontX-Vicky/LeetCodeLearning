def singleNumber(nums: list[int]) -> int:
    # XOR trick: x ^ x = 0, x ^ 0 = x
    # XOR all numbers together — duplicates cancel out, lone element remains
    result = 0
    for n in nums:
        result ^= n
    return result

def hammingWeight(n: int) -> int:
    # Brian Kernighan's algorithm
    # n & (n - 1) clears the lowest set bit of n
    count = 0
    while n:
        n &= n - 1  # Drop the lowest set bit
        count += 1
    return count
