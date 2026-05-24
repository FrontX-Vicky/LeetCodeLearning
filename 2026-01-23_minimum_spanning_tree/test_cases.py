# Test Cases - Comprehensive Testing for Minimum Spanning Tree

from main import (
    minCostConnectPoints,
    minimumSpanningTree,
    minCostToSupplyWater,
    findCriticalAndPseudoCriticalEdges,
    minimumCost,
)


def test_minCostConnectPoints():
    print("Testing minCostConnectPoints (#1584):")
    cases = [
        ([[0,0],[2,2],[3,10],[5,2],[7,0]],          20, "canonical 5 points"),
        ([[3,12],[-2,5],[-4,1]],                    18, "3 points negative coords"),
        ([[0,0],[1,1],[1,0],[-1,1]],                 4, "4 points close together"),
        ([[0,0]],                                    0, "single point"),
        ([[0,0],[1,0]],                              1, "two points"),
    ]

    passed = 0
    for points, expected, desc in cases:
        result = minCostConnectPoints(points)
        ok = result == expected
        print(f"  [{'PASS' if ok else 'FAIL'}] {desc}: got {result}, expected {expected}")
        if ok:
            passed += 1
    print(f"  Summary: {passed}/{len(cases)} passed\n")
    return passed, len(cases)


def test_minimumSpanningTree():
    print("Testing minimumSpanningTree (Kruskal's):")
    cases = [
        ((4, [[0,1,1],[1,2,2],[0,2,4],[2,3,3]]),  6,  "4 nodes, skip heavy edge"),
        ((4, [[0,1,1],[0,2,2],[0,3,3]]),            6,  "star graph"),
        ((3, [[0,1,5],[1,2,3],[0,2,6]]),            8,  "triangle, skip heaviest"),
        ((2, [[0,1,7]]),                             7,  "two nodes one edge"),
        ((3, [[0,1,1]]),                            -1,  "disconnected graph"),
    ]

    passed = 0
    for (n, edges), expected, desc in cases:
        result = minimumSpanningTree(n, edges)
        ok = result == expected
        print(f"  [{'PASS' if ok else 'FAIL'}] {desc}: got {result}, expected {expected}")
        if ok:
            passed += 1
    print(f"  Summary: {passed}/{len(cases)} passed\n")
    return passed, len(cases)


def test_minCostToSupplyWater():
    print("Testing minCostToSupplyWater (#1168):")
    cases = [
        ((3, [1,2,2], [[1,2,1],[2,3,1]]),         3, "canonical: well+2 pipes"),
        ((2, [1,1],   [[1,2,10]]),                 2, "two cheap wells vs expensive pipe"),
        ((1, [5],     []),                          5, "single house, must drill"),
        ((3, [10,10,10], [[1,2,1],[2,3,1]]),       12, "pipes cheaper than wells"),
        ((2, [3,4],   [[1,2,2]]),                   5, "drill house1 + pipe to house2"),
    ]

    passed = 0
    for (n, wells, pipes), expected, desc in cases:
        result = minCostToSupplyWater(n, wells, pipes)
        ok = result == expected
        print(f"  [{'PASS' if ok else 'FAIL'}] {desc}: got {result}, expected {expected}")
        if ok:
            passed += 1
    print(f"  Summary: {passed}/{len(cases)} passed\n")
    return passed, len(cases)


def test_findCriticalAndPseudoCriticalEdges():
    print("Testing findCriticalAndPseudoCriticalEdges (#1489):")
    cases = [
        (
            (5, [[0,1,1],[1,2,1],[2,3,2],[0,3,2],[0,4,3],[3,4,3],[1,4,6]]),
            [[0,1],[2,3,4,5]],
            "canonical 5 nodes"
        ),
        (
            (4, [[0,1,1],[1,2,1],[2,3,1],[0,3,1]]),
            [[], [0,1,2,3]],
            "all equal weight — no critical edges"
        ),
        (
            (3, [[0,1,1],[1,2,2],[0,2,3]]),
            [[0,1], []],
            "path graph — both edges critical"
        ),
    ]

    passed = 0
    for (n, edges), expected, desc in cases:
        result = findCriticalAndPseudoCriticalEdges(n, edges)
        ok = result == expected
        print(f"  [{'PASS' if ok else 'FAIL'}] {desc}: got {result}, expected {expected}")
        if ok:
            passed += 1
    print(f"  Summary: {passed}/{len(cases)} passed\n")
    return passed, len(cases)


def test_minimumCost():
    print("Testing minimumCost (#1135):")
    cases = [
        ((3, [[1,2,5],[1,3,6],[2,3,1]]),   6,  "canonical 3 cities"),
        ((4, [[1,2,3],[3,4,4],[1,4,3],[1,3,1],[2,4,1]]),  6, "4 cities dense"),
        ((3, [[1,2,1],[2,3,2]]),            3,  "chain, both edges needed"),
        ((4, [[1,2,1],[2,3,2]]),           -1,  "city 4 unreachable"),
        ((2, [[1,2,100]]),               100,  "two cities one edge"),
    ]

    passed = 0
    for (n, connections), expected, desc in cases:
        result = minimumCost(n, connections)
        ok = result == expected
        print(f"  [{'PASS' if ok else 'FAIL'}] {desc}: got {result}, expected {expected}")
        if ok:
            passed += 1
    print(f"  Summary: {passed}/{len(cases)} passed\n")
    return passed, len(cases)


def run_all_tests():
    print("=" * 70)
    print("DAY 23 - MINIMUM SPANNING TREE TEST SUITE")
    print("=" * 70 + "\n")

    total_passed = 0
    total_tests  = 0

    for fn in [
        test_minCostConnectPoints,
        test_minimumSpanningTree,
        test_minCostToSupplyWater,
        test_findCriticalAndPseudoCriticalEdges,
        test_minimumCost,
    ]:
        p, t = fn()
        total_passed += p
        total_tests  += t

    print("=" * 70)
    print(f"TOTAL: {total_passed}/{total_tests} tests passed")
    print("=" * 70)


if __name__ == "__main__":
    run_all_tests()
