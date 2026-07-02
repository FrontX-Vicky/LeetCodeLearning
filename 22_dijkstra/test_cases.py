# Test Cases - Comprehensive Testing for Dijkstra's Shortest Path

from main import (
    networkDelayTime,
    findCheapestPrice,
    minimumEffortPath,
    swimInWater,
    findTheCity,
)


def test_networkDelayTime():
    print("Testing networkDelayTime (#743):")
    cases = [
        (([[2,1,1],[2,3,1],[3,4,1]], 4, 2), 2,   "canonical example"),
        (([[1,2,1]], 2, 1),                  1,   "two nodes"),
        (([[1,2,1]], 2, 2),                 -1,   "source isolated from node 1"),
        (([[1,2,1],[2,3,2],[1,3,4]], 3, 1),  3,   "two paths to node 3"),
        (([],  1, 1),                         0,   "single node"),
    ]

    passed = 0
    for (times, n, k), expected, desc in cases:
        result = networkDelayTime(times, n, k)
        ok = result == expected
        print(f"  [{'PASS' if ok else 'FAIL'}] {desc}: got {result}, expected {expected}")
        if ok:
            passed += 1

    print(f"  Summary: {passed}/{len(cases)} passed\n")
    return passed, len(cases)


def test_findCheapestPrice():
    print("Testing findCheapestPrice (#787):")
    cases = [
        ((4, [[0,1,100],[1,2,100],[2,0,100],[1,3,600],[2,3,200]], 0, 3, 1), 700, "canonical k=1"),
        ((3, [[0,1,100],[1,2,100],[0,2,500]], 0, 2, 1),                     200, "k=1 direct cheaper via 2 hops"),
        ((3, [[0,1,100],[1,2,100],[0,2,500]], 0, 2, 0),                     500, "k=0 direct only"),
        ((3, [[0,1,100],[1,2,100]], 0, 2, 0),                                -1, "no direct route, k=0"),
        ((1, [], 0, 0, 0),                                                    0, "src == dst"),
    ]

    passed = 0
    for (n, flights, src, dst, k), expected, desc in cases:
        result = findCheapestPrice(n, flights, src, dst, k)
        ok = result == expected
        print(f"  [{'PASS' if ok else 'FAIL'}] {desc}: got {result}, expected {expected}")
        if ok:
            passed += 1

    print(f"  Summary: {passed}/{len(cases)} passed\n")
    return passed, len(cases)


def test_minimumEffortPath():
    print("Testing minimumEffortPath (#1631):")
    cases = [
        ([[1,2,2],[3,8,2],[5,3,5]],                   2, "canonical 3x3"),
        ([[1,2,3],[3,8,4],[5,3,5]],                   1, "3x3 alternate path"),
        ([[1,2,1,1,1],[1,2,1,2,1],[1,2,1,2,1],[1,2,1,2,1],[1,1,1,2,1]], 0, "5x5 zero effort"),
        ([[1]],                                        0, "single cell"),
        ([[1,1000000000]],                    999999999, "single row large gap"),
    ]

    passed = 0
    for heights, expected, desc in cases:
        result = minimumEffortPath(heights)
        ok = result == expected
        print(f"  [{'PASS' if ok else 'FAIL'}] {desc}: got {result}, expected {expected}")
        if ok:
            passed += 1

    print(f"  Summary: {passed}/{len(cases)} passed\n")
    return passed, len(cases)


def test_swimInWater():
    print("Testing swimInWater (#778):")
    cases = [
        ([[0,2],[1,3]],                       3, "2x2 canonical"),
        ([[0,1,2,3,4],[24,23,22,21,5],[12,13,14,15,16],[11,17,18,19,20],[10,9,8,7,6]], 16, "5x5 spiral"),
        ([[0]],                               0, "single cell"),
        ([[0,1],[2,3]],                       3, "2x2 need to wait for 3"),
        ([[3,2],[0,1]],                       3, "2x2 top-left starts at 3"),
    ]

    passed = 0
    for grid, expected, desc in cases:
        result = swimInWater(grid)
        ok = result == expected
        print(f"  [{'PASS' if ok else 'FAIL'}] {desc}: got {result}, expected {expected}")
        if ok:
            passed += 1

    print(f"  Summary: {passed}/{len(cases)} passed\n")
    return passed, len(cases)


def test_findTheCity():
    print("Testing findTheCity (#1334):")
    cases = [
        ((4, [[0,1,3],[1,2,1],[1,3,4],[2,3,1]], 4),   3, "canonical example"),
        ((5, [[0,1,2],[0,4,8],[1,2,3],[1,4,2],[2,3,1],[3,4,1]], 2), 0, "5 cities threshold=2"),
        ((2, [[0,1,1]], 1),                             1, "two cities tie -> higher index"),
        ((3, [[0,1,1],[1,2,1]], 2),                     2, "chain, threshold=2 -> all tie at 2, ties -> highest index 2"),
        ((4, [[0,1,1],[1,2,1],[2,3,1],[0,3,10]], 3),   3, "tie at far city"),
    ]

    passed = 0
    for (n, edges, threshold), expected, desc in cases:
        result = findTheCity(n, edges, threshold)
        ok = result == expected
        print(f"  [{'PASS' if ok else 'FAIL'}] {desc}: got {result}, expected {expected}")
        if ok:
            passed += 1

    print(f"  Summary: {passed}/{len(cases)} passed\n")
    return passed, len(cases)


def run_all_tests():
    print("=" * 70)
    print("DAY 22 - DIJKSTRA'S SHORTEST PATH TEST SUITE")
    print("=" * 70)

    total_passed = 0
    total_tests = 0

    for fn in [
        test_networkDelayTime,
        test_findCheapestPrice,
        test_minimumEffortPath,
        test_swimInWater,
        test_findTheCity,
    ]:
        p, t = fn()
        total_passed += p
        total_tests += t

    print("=" * 70)
    print(f"TOTAL: {total_passed}/{total_tests} tests passed")
    print("=" * 70)


if __name__ == "__main__":
    run_all_tests()
