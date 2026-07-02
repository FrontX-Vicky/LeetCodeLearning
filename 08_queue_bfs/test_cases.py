# Test Cases for Recent Counter (Queue)

from main import RecentCounterList, RecentCounterDeque, RecentCounterWindow

def test_approach(CounterClass, name):
    """Test a RecentCounter implementation"""
    print(f"Testing {name}:")
    
    # Test 1: Basic example from problem
    rc = CounterClass()
    result = []
    result.append(rc.ping(1))
    result.append(rc.ping(100))
    result.append(rc.ping(3001))
    result.append(rc.ping(3002))
    expected = [1, 2, 3, 3]
    status = "PASS" if result == expected else "FAIL"
    print(f"  [{status}] Test 1: Basic example -> {result} (expected {expected})")
    
    # Test 2: All requests outside window
    rc = CounterClass()
    result = []
    result.append(rc.ping(1))
    result.append(rc.ping(3500))
    result.append(rc.ping(7000))
    result.append(rc.ping(10500))
    expected = [1, 1, 1, 1]
    status = "PASS" if result == expected else "FAIL"
    print(f"  [{status}] Test 2: Requests outside window -> {result} (expected {expected})")
    
    # Test 3: All requests inside window
    rc = CounterClass()
    result = []
    result.append(rc.ping(1))
    result.append(rc.ping(500))
    result.append(rc.ping(1000))
    result.append(rc.ping(1500))
    result.append(rc.ping(2000))
    expected = [1, 2, 3, 4, 5]
    status = "PASS" if result == expected else "FAIL"
    print(f"  [{status}] Test 3: All inside window -> {result} (expected {expected})")
    
    # Test 4: Gradual expiration
    rc = CounterClass()
    result = []
    result.append(rc.ping(1))
    result.append(rc.ping(1000))
    result.append(rc.ping(2000))
    result.append(rc.ping(3000))
    result.append(rc.ping(4000))  # 1 expires (4000-3000=1000 > 1)
    result.append(rc.ping(5000))  # 1000 expires
    expected = [1, 2, 3, 4, 4, 4]
    status = "PASS" if result == expected else "FAIL"
    print(f"  [{status}] Test 4: Gradual expiration -> {result} (expected {expected})")
    
    # Test 5: Window boundary (exactly 3000ms)
    rc = CounterClass()
    result = []
    result.append(rc.ping(1))
    result.append(rc.ping(3001))  # 1 is at boundary (3001-3000=1)
    result.append(rc.ping(6001))  # 3001 is at boundary
    expected = [1, 2, 2]
    status = "PASS" if result == expected else "FAIL"
    print(f"  [{status}] Test 5: Window boundary -> {result} (expected {expected})")
    
    # Test 6: Single request
    rc = CounterClass()
    result = rc.ping(100)
    expected = 1
    status = "PASS" if result == expected else "FAIL"
    print(f"  [{status}] Test 6: Single request -> {result} (expected {expected})")
    
    # Test 7: Large time gap
    rc = CounterClass()
    result = []
    result.append(rc.ping(1))
    result.append(rc.ping(1000000))  # Very large gap
    expected = [1, 1]
    status = "PASS" if result == expected else "FAIL"
    print(f"  [{status}] Test 7: Large time gap -> {result} (expected {expected})")
    
    # Test 8: Many requests in window
    rc = CounterClass()
    result = []
    for i in range(1, 11):  # 10 requests within 10ms
        result.append(rc.ping(i))
    expected = list(range(1, 11))  # [1, 2, 3, ..., 10]
    status = "PASS" if result == expected else "FAIL"
    print(f"  [{status}] Test 8: Many requests in window -> {result} (expected {expected})")
    
    # Test 9: Alternating inside/outside window
    rc = CounterClass()
    result = []
    result.append(rc.ping(1))
    result.append(rc.ping(10))
    result.append(rc.ping(4000))  # 1 and 10 expire
    result.append(rc.ping(4010))
    result.append(rc.ping(7500))  # 4000 and 4010 expire
    expected = [1, 2, 1, 2, 1]
    status = "PASS" if result == expected else "FAIL"
    print(f"  [{status}] Test 9: Alternating window -> {result} (expected {expected})")
    
    # Test 10: Stress test (many requests)
    rc = CounterClass()
    result = []
    # Add 100 requests at t=1 to t=100
    for i in range(1, 101):
        result.append(rc.ping(i))
    # At t=100, window is [-2900, 100], so all 100 requests are valid
    status = "PASS" if result[-1] == 100 else "FAIL"
    print(f"  [{status}] Test 10: Stress test (100 requests) -> last count {result[-1]} (expected 100)")
    
    print()


def run_all_tests():
    print("=" * 60)
    print("LEETCODE #933: NUMBER OF RECENT CALLS - TEST SUITE")
    print("=" * 60)
    print()
    
    test_approach(RecentCounterList, "RecentCounterList (List-based)")
    test_approach(RecentCounterDeque, "RecentCounterDeque (Optimized)")
    test_approach(RecentCounterWindow, "RecentCounterWindow (Explicit Window)")
    
    print("=" * 60)
    print("TOTAL: 30 tests (3 approaches × 10 test cases)")
    print("=" * 60)


if __name__ == "__main__":
    run_all_tests()
