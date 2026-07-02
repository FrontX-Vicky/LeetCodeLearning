# Test Cases - Comprehensive Testing for Topological Sort

from main import (
    canFinish,
    findOrder,
    alienOrder,
    findMinHeightTrees,
    minimumSemesters,
)


def _is_valid_topo_order(order, numCourses, prerequisites):
    if len(order) != numCourses:
        return False
    pos = {course: i for i, course in enumerate(order)}
    for course, prereq in prerequisites:
        if pos[prereq] > pos[course]:
            return False
    return True


def test_canFinish():
    print("Testing canFinish (#207):")
    cases = [
        (2, [[1, 0]], True, "simple chain"),
        (2, [[1, 0], [0, 1]], False, "2-cycle"),
        (4, [[1, 0], [2, 1], [3, 2]], True, "long chain"),
        (4, [[1, 0], [2, 1], [0, 2]], False, "3-cycle"),
        (3, [], True, "no prerequisites"),
    ]

    passed = 0
    for n, pre, expected, desc in cases:
        result = canFinish(n, pre)
        ok = result == expected
        print(f"  [{'PASS' if ok else 'FAIL'}] {desc}: got {result}, expected {expected}")
        if ok:
            passed += 1

    print(f"  Summary: {passed}/{len(cases)} passed\n")
    return passed, len(cases)


def test_findOrder():
    print("Testing findOrder (#210):")
    cases = [
        (2, [[1, 0]], True, "simple chain"),
        (2, [[1, 0], [0, 1]], False, "cycle -> empty"),
        (4, [[1, 0], [2, 0], [3, 1], [3, 2]], True, "branching DAG"),
        (1, [], True, "single course"),
        (3, [], True, "independent courses"),
    ]

    passed = 0
    for n, pre, should_exist, desc in cases:
        order = findOrder(n, pre)
        if should_exist:
            ok = _is_valid_topo_order(order, n, pre)
        else:
            ok = order == []

        print(f"  [{'PASS' if ok else 'FAIL'}] {desc}: order={order}")
        if ok:
            passed += 1

    print(f"  Summary: {passed}/{len(cases)} passed\n")
    return passed, len(cases)


def test_alienOrder():
    print("Testing alienOrder (#269):")
    cases = [
        (["wrt", "wrf", "er", "ett", "rftt"], "wertf", True, "canonical example"),
        (["z", "x"], "zx", True, "simple 2-char order"),
        (["z", "x", "z"], "", False, "cycle in character graph"),
        (["abc", "ab"], "", False, "invalid prefix rule"),
        (["a"], "a", True, "single word"),
    ]

    passed = 0
    for words, expected_example, has_solution, desc in cases:
        order = alienOrder(words)

        if not has_solution:
            ok = order == ""
        else:
            # At least ensure all unique chars are present and no empty answer.
            chars = set("".join(words))
            ok = len(order) == len(chars) and set(order) == chars

        print(f"  [{'PASS' if ok else 'FAIL'}] {desc}: order='{order}'")
        if ok:
            passed += 1

    print(f"  Summary: {passed}/{len(cases)} passed\n")
    return passed, len(cases)


def test_findMinHeightTrees():
    print("Testing findMinHeightTrees (#310):")
    cases = [
        (1, [], [0], "single node"),
        (2, [[0, 1]], [0, 1], "two nodes"),
        (4, [[1, 0], [1, 2], [1, 3]], [1], "star"),
        (6, [[3, 0], [3, 1], [3, 2], [3, 4], [5, 4]], [3, 4], "two centroids"),
        (5, [[0, 1], [1, 2], [2, 3], [3, 4]], [2], "line graph"),
    ]

    passed = 0
    for n, edges, expected, desc in cases:
        result = sorted(findMinHeightTrees(n, edges))
        ok = result == sorted(expected)
        print(f"  [{'PASS' if ok else 'FAIL'}] {desc}: got {result}, expected {expected}")
        if ok:
            passed += 1

    print(f"  Summary: {passed}/{len(cases)} passed\n")
    return passed, len(cases)


def test_minimumSemesters():
    print("Testing minimumSemesters (#1136):")
    cases = [
        (3, [[1, 3], [2, 3]], 2, "two prerequisites then final"),
        (3, [[1, 2], [2, 3], [3, 1]], -1, "cycle"),
        (4, [[2, 1], [3, 1], [1, 4]], 3, "layered"),
        (4, [], 1, "all independent"),
        (1, [], 1, "single course"),
    ]

    passed = 0
    for n, rel, expected, desc in cases:
        result = minimumSemesters(n, rel)
        ok = result == expected
        print(f"  [{'PASS' if ok else 'FAIL'}] {desc}: got {result}, expected {expected}")
        if ok:
            passed += 1

    print(f"  Summary: {passed}/{len(cases)} passed\n")
    return passed, len(cases)


def run_all_tests():
    print("=" * 70)
    print("DAY 21 - TOPOLOGICAL SORT TEST SUITE")
    print("=" * 70)

    total_passed = 0
    total_tests = 0

    for fn in [
        test_canFinish,
        test_findOrder,
        test_alienOrder,
        test_findMinHeightTrees,
        test_minimumSemesters,
    ]:
        p, t = fn()
        total_passed += p
        total_tests += t

    print("=" * 70)
    print(f"TOTAL: {total_passed}/{total_tests} tests passed")
    print("=" * 70)


if __name__ == "__main__":
    run_all_tests()
