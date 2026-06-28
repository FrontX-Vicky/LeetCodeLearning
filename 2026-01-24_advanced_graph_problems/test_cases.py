from main import findItinerary, isBipartite, ladderLength, criticalConnections

def test_findItinerary():
    print("Testing findItinerary (#332):")
    cases = [
        ([["MUC","LHR"],["JFK","MUC"],["SFO","SJC"],["LHR","SFO"]], ["JFK","MUC","LHR","SFO","SJC"], "simple path"),
        ([["JFK","SFO"],["JFK","ATL"],["SFO","ATL"],["ATL","JFK"],["ATL","SFO"]], ["JFK","ATL","JFK","SFO","ATL","SFO"], "lexical order choice")
    ]
    passed = 0
    for tickets, expected, desc in cases:
        result = findItinerary(tickets)
        ok = result == expected
        print(f"  [{'PASS' if ok else 'FAIL'}] {desc}: got {result}, expected {expected}")
        if ok: passed += 1
    print(f"  Summary: {passed}/{len(cases)} passed\n")
    return passed, len(cases)

def test_isBipartite():
    print("Testing isBipartite (#785):")
    cases = [
        ([[1,2,3],[0,2],[0,1,3],[0,2]], False, "not bipartite (odd cycle)"),
        ([[1,3],[0,2],[1,3],[0,2]], True, "bipartite (even cycle)")
    ]
    passed = 0
    for graph, expected, desc in cases:
        result = isBipartite(graph)
        ok = result == expected
        print(f"  [{'PASS' if ok else 'FAIL'}] {desc}: got {result}, expected {expected}")
        if ok: passed += 1
    print(f"  Summary: {passed}/{len(cases)} passed\n")
    return passed, len(cases)

def test_ladderLength():
    print("Testing ladderLength (#127):")
    cases = [
        ("hit", "cog", ["hot","dot","dog","lot","log","cog"], 5, "standard transformation"),
        ("hit", "cog", ["hot","dot","dog","lot","log"], 0, "endWord not in dict")
    ]
    passed = 0
    for b, e, wl, expected, desc in cases:
        result = ladderLength(b, e, wl)
        ok = result == expected
        print(f"  [{'PASS' if ok else 'FAIL'}] {desc}: got {result}, expected {expected}")
        if ok: passed += 1
    print(f"  Summary: {passed}/{len(cases)} passed\n")
    return passed, len(cases)

def test_criticalConnections():
    print("Testing criticalConnections (#1192):")
    cases = [
        (4, [[0,1],[1,2],[2,0],[1,3]], [[1,3]], "single critical edge"),
        (2, [[0,1]], [[0,1]], "two nodes, one edge")
    ]
    passed = 0
    for n, connections, expected, desc in cases:
        result = criticalConnections(n, connections)
        # order of edges and nodes within edges doesn't matter, normalize for comparison
        res_norm = sorted([sorted(e) for e in result])
        exp_norm = sorted([sorted(e) for e in expected])
        ok = res_norm == exp_norm
        print(f"  [{'PASS' if ok else 'FAIL'}] {desc}: got {result}, expected {expected}")
        if ok: passed += 1
    print(f"  Summary: {passed}/{len(cases)} passed\n")
    return passed, len(cases)

def run_all_tests():
    print("DAY 24 - ADVANCED GRAPH PROBLEMS TEST SUITE")
    print("=" * 70 + "\n")
    
    total_passed = 0
    total_tests = 0
    
    for fn in [test_findItinerary, test_isBipartite, test_ladderLength, test_criticalConnections]:
        p, t = fn()
        total_passed += p
        total_tests += t
        
    print("=" * 70)
    print(f"TOTAL: {total_passed}/{total_tests} tests passed")
    print("=" * 70)

if __name__ == "__main__":
    run_all_tests()
