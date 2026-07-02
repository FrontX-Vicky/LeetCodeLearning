# Test Cases - Comprehensive Testing for Union Find

from main import (
    UnionFind,
    findCircleNum,
    findRedundantConnection,
    validTree,
    countComponents,
    accountsMerge,
)


# ============================================================
# UNION FIND CORE TESTS
# ============================================================

def test_union_find_core():
    print("Testing UnionFind Core:")
    passed = 0

    tests = [
        {
            "desc": "Basic union and connectivity",
            "n": 5,
            "unions": [(0, 1), (1, 2), (3, 4)],
            "checks": [(0, 2, True), (0, 3, False), (3, 4, True), (1, 3, False)],
            "components": 2,
        },
        {
            "desc": "All nodes isolated",
            "n": 4,
            "unions": [],
            "checks": [(0, 1, False), (2, 3, False), (1, 3, False)],
            "components": 4,
        },
        {
            "desc": "All nodes connected",
            "n": 4,
            "unions": [(0, 1), (1, 2), (2, 3)],
            "checks": [(0, 3, True), (1, 3, True), (0, 2, True)],
            "components": 1,
        },
        {
            "desc": "Cycle: union same component returns False",
            "n": 3,
            "unions": [(0, 1), (1, 2)],
            "checks": [(0, 2, True)],
            "components": 1,
        },
        {
            "desc": "Path compression: long chain",
            "n": 8,
            "unions": [(0, 1), (1, 2), (2, 3), (3, 4), (4, 5), (5, 6), (6, 7)],
            "checks": [(0, 7, True), (0, 4, True), (2, 6, True)],
            "components": 1,
        },
        {
            "desc": "Union return values (cycle detection)",
            "n": 3,
            "unions": [],
            "checks": [],
            "components": 3,
            "union_returns": [(0, 1, True), (1, 2, True), (0, 2, False)],
        },
    ]

    total = len(tests)
    for test in tests:
        uf = UnionFind(test["n"])
        ok = True

        for x, y in test.get("unions", []):
            uf.union(x, y)

        for x, y, expected_ret in test.get("union_returns", []):
            ret = uf.union(x, y)
            if ret != expected_ret:
                ok = False
                print(f"  [FAIL] {test['desc']}: union({x},{y}) expected {expected_ret}, got {ret}")

        for x, y, expected_conn in test["checks"]:
            if uf.connected(x, y) != expected_conn:
                ok = False
                print(f"  [FAIL] {test['desc']}: connected({x},{y}) expected {expected_conn}")

        if uf.components != test["components"]:
            ok = False
            print(f"  [FAIL] {test['desc']}: components expected {test['components']}, got {uf.components}")

        if ok:
            print(f"  [PASS] {test['desc']}")
            passed += 1

    print(f"  UnionFind Core: {passed}/{total}\n")
    return passed, total


# ============================================================
# PROBLEM 1: NUMBER OF PROVINCES
# ============================================================

def test_findCircleNum():
    print("Testing findCircleNum (Number of Provinces):")
    passed = 0

    cases = [
        ([[1, 1, 0], [1, 1, 0], [0, 0, 1]], 2, "Two provinces: {0,1} and {2}"),
        ([[1, 0, 0], [0, 1, 0], [0, 0, 1]], 3, "All isolated: 3 provinces"),
        ([[1, 1, 1], [1, 1, 1], [1, 1, 1]], 1, "All connected: 1 province"),
        ([[1, 0], [0, 1]], 2, "2 nodes, no edge"),
        ([[1, 1], [1, 1]], 1, "2 nodes, connected"),
        (
            [[1, 0, 0, 1], [0, 1, 1, 0], [0, 1, 1, 0], [1, 0, 0, 1]],
            2,
            "4 cities, 2 provinces",
        ),
        (
            [[1, 0, 0, 0, 0], [0, 1, 0, 0, 0], [0, 0, 1, 0, 0],
             [0, 0, 0, 1, 0], [0, 0, 0, 0, 1]],
            5,
            "5 isolated cities",
        ),
        ([[1]], 1, "Single city"),
    ]

    for isConnected, expected, desc in cases:
        result = findCircleNum(isConnected)
        status = "PASS" if result == expected else "FAIL"
        print(f"  [{status}] {desc}: got {result}, expected {expected}")
        if result == expected:
            passed += 1

    print(f"  findCircleNum: {passed}/{len(cases)}\n")
    return passed, len(cases)


# ============================================================
# PROBLEM 2: REDUNDANT CONNECTION
# ============================================================

def test_findRedundantConnection():
    print("Testing findRedundantConnection:")
    passed = 0

    cases = [
        ([[1, 2], [1, 3], [2, 3]], [2, 3], "Triangle: [2,3] redundant"),
        ([[1, 2], [2, 3], [3, 4], [1, 4], [1, 5]], [1, 4], "Chain + shortcut"),
        ([[1, 2], [2, 3], [3, 1]], [3, 1], "Direct triangle [3,1]"),
        ([[1, 2], [1, 3], [1, 4], [3, 4]], [3, 4], "Star with extra edge"),
        ([[1, 2], [2, 3], [1, 3]], [1, 3], "Triangle [1,3] closes it"),
    ]

    for edges, expected, desc in cases:
        result = findRedundantConnection(edges)
        status = "PASS" if result == expected else "FAIL"
        print(f"  [{status}] {desc}: got {result}, expected {expected}")
        if result == expected:
            passed += 1

    print(f"  findRedundantConnection: {passed}/{len(cases)}\n")
    return passed, len(cases)


# ============================================================
# PROBLEM 3: GRAPH VALID TREE
# ============================================================

def test_validTree():
    print("Testing validTree:")
    passed = 0

    cases = [
        (5, [[0, 1], [0, 2], [0, 3], [1, 4]], True, "Star tree"),
        (5, [[0, 1], [1, 2], [2, 3], [1, 3], [1, 4]], False, "Has cycle"),
        (1, [], True, "Single node, no edges"),
        (2, [[0, 1]], True, "Two nodes, one edge"),
        (2, [], False, "Two nodes, no edge (disconnected)"),
        (3, [[0, 1], [1, 2]], True, "Linear chain"),
        (3, [[0, 1], [1, 2], [0, 2]], False, "Triangle (cycle)"),
        (4, [[0, 1], [2, 3]], False, "Two disconnected components"),
        (4, [[0, 1], [1, 2], [2, 3]], True, "Path graph"),
        (4, [[0, 1], [0, 2], [0, 3]], True, "Star with 3 leaves"),
    ]

    for n, edges, expected, desc in cases:
        result = validTree(n, edges)
        status = "PASS" if result == expected else "FAIL"
        print(f"  [{status}] n={n}: {desc}: got {result}, expected {expected}")
        if result == expected:
            passed += 1

    print(f"  validTree: {passed}/{len(cases)}\n")
    return passed, len(cases)


# ============================================================
# PROBLEM 4: COUNT COMPONENTS
# ============================================================

def test_countComponents():
    print("Testing countComponents:")
    passed = 0

    cases = [
        (5, [[0, 1], [1, 2], [3, 4]], 2, "Two components: {0,1,2} and {3,4}"),
        (5, [[0, 1], [1, 2], [2, 3], [3, 4]], 1, "All connected"),
        (5, [], 5, "No edges: 5 isolated nodes"),
        (1, [], 1, "Single node"),
        (4, [[0, 1], [2, 3]], 2, "Two pairs"),
        (6, [[0, 1], [0, 2], [3, 4], [3, 5]], 2, "Two triangles"),
        (3, [[0, 1], [0, 2], [1, 2]], 1, "Triangle"),
        (2, [[0, 1]], 1, "Two nodes connected"),
        (2, [], 2, "Two nodes disconnected"),
    ]

    for n, edges, expected, desc in cases:
        result = countComponents(n, edges)
        status = "PASS" if result == expected else "FAIL"
        print(f"  [{status}] {desc}: got {result}, expected {expected}")
        if result == expected:
            passed += 1

    print(f"  countComponents: {passed}/{len(cases)}\n")
    return passed, len(cases)


# ============================================================
# PROBLEM 5: ACCOUNTS MERGE
# ============================================================

def test_accountsMerge():
    print("Testing accountsMerge:")
    passed = 0

    # Helper: convert result to a canonical form for comparison
    def normalize(result):
        """Sort each account's emails, sort accounts by first email"""
        normalized = []
        for acc in result:
            normalized.append([acc[0]] + sorted(acc[1:]))
        return sorted(normalized, key=lambda a: a[1] if len(a) > 1 else "")

    # Test 1: Standard LeetCode example
    accounts1 = [
        ["John", "johnsmith@mail.com", "john_newyork@mail.com"],
        ["John", "johnsmith@mail.com", "john00@mail.com"],
        ["Mary", "mary@mail.com"],
        ["John", "johnnybravo@mail.com"],
    ]
    result1 = accountsMerge(accounts1)
    ok1 = len(result1) == 3 and sum(len(a) - 1 for a in result1) == 5
    status1 = "PASS" if ok1 else "FAIL"
    print(f"  [{status1}] Standard example: {len(result1)} accounts (expected 3), "
          f"{sum(len(a)-1 for a in result1)} total emails (expected 5)")
    if ok1:
        passed += 1

    # Test 2: No merging needed
    accounts2 = [
        ["Alice", "alice@mail.com"],
        ["Bob", "bob@mail.com"],
        ["Carol", "carol@mail.com"],
    ]
    result2 = accountsMerge(accounts2)
    ok2 = len(result2) == 3
    status2 = "PASS" if ok2 else "FAIL"
    print(f"  [{status2}] No merging: {len(result2)} accounts (expected 3)")
    if ok2:
        passed += 1

    # Test 3: Chain merge (a–b, b–c, c–d → all one account)
    accounts3 = [
        ["Alex", "a@m.com", "b@m.com"],
        ["Alex", "b@m.com", "c@m.com"],
        ["Alex", "c@m.com", "d@m.com"],
    ]
    result3 = accountsMerge(accounts3)
    ok3 = len(result3) == 1 and len(result3[0]) == 5  # name + 4 emails
    status3 = "PASS" if ok3 else "FAIL"
    emails3 = len(result3[0]) - 1 if result3 else 0
    print(f"  [{status3}] Chain merge: {len(result3)} account(s), "
          f"{emails3} emails (expected 1 account, 4 emails)")
    if ok3:
        passed += 1

    # Test 4: Single account
    accounts4 = [["Dave", "dave@mail.com"]]
    result4 = accountsMerge(accounts4)
    ok4 = len(result4) == 1 and result4[0][0] == "Dave" and result4[0][1] == "dave@mail.com"
    status4 = "PASS" if ok4 else "FAIL"
    print(f"  [{status4}] Single account: {result4}")
    if ok4:
        passed += 1

    # Test 5: Two accounts same person with 3 emails each sharing 1
    accounts5 = [
        ["Emma", "em1@x.com", "em2@x.com"],
        ["Emma", "em2@x.com", "em3@x.com"],
    ]
    result5 = accountsMerge(accounts5)
    ok5 = len(result5) == 1 and len(result5[0]) == 4  # name + 3 emails
    status5 = "PASS" if ok5 else "FAIL"
    print(f"  [{status5}] Two-account merge via shared email: "
          f"{len(result5)} account, {len(result5[0])-1 if result5 else 0} emails (expected 1, 3)")
    if ok5:
        passed += 1

    print(f"  accountsMerge: {passed}/5\n")
    return passed, 5


# ============================================================
# RUN ALL TESTS
# ============================================================

def run_all_tests():
    print("=" * 70)
    print("LEETCODE UNION FIND - TEST SUITE")
    print("=" * 70)
    print()

    total_passed = 0
    total_tests = 0

    p, t = test_union_find_core()
    total_passed += p
    total_tests += t

    p, t = test_findCircleNum()
    total_passed += p
    total_tests += t

    p, t = test_findRedundantConnection()
    total_passed += p
    total_tests += t

    p, t = test_validTree()
    total_passed += p
    total_tests += t

    p, t = test_countComponents()
    total_passed += p
    total_tests += t

    p, t = test_accountsMerge()
    total_passed += p
    total_tests += t

    print("=" * 70)
    print(f"TOTAL: {total_passed}/{total_tests} tests passed")
    print("=" * 70)


if __name__ == "__main__":
    run_all_tests()
