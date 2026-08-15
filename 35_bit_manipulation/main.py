def singleNumber(nums: list[int]) -> int:
    """
    Given a non-empty array of integers nums, every element appears twice except for one.
    Find that single one.
    You must implement a solution with O(n) runtime complexity and use O(1) extra space.
    """
    result = 0
    for n in nums:
        result ^= n 
    return result

def hammingWeight(n: int) -> int:
    """
    Given a positive integer n, write a function that returns the number of set bits
    in its binary representation (also known as the Hamming weight or popcount).
    """
    count = 0
    while n:
        n &= n - 1
        count += 1
    return count

def main():
    print("Welcome to Day 35: Bit Manipulation!")
    print("Run `python test_cases.py` to check your implementations.")

if __name__ == "__main__":
    main()
