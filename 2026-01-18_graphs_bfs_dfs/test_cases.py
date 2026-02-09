# Test Cases for Graph BFS & DFS Problems
# Run: python test_cases.py

from main import (
    num_islands, clone_graph, pacific_atlantic,
    can_finish, solve, oranges_rotting, Node
)
import sys


class TestRunner:
    def __init__(self):
        self.tests_run = 0
        self.tests_passed = 0
        self.current_problem = ""
    
    def set_problem(self, name):
        self.current_problem = name
        print(f"\n{'=' * 60}")
        print(f"Testing: {name}")
        print('=' * 60)
    
    def test(self, func, inputs, expected, test_name):
        self.tests_run += 1
        try:
            if isinstance(inputs, tuple):
                result = func(*inputs)
            else:
                result = func(inputs)
            
            # Special comparison for list of lists
            if isinstance(result, list) and result and isinstance(result[0], list):
                result = sorted([sorted(x) for x in result])
                expected = sorted([sorted(x) for x in expected])
            
            passed = result == expected
            
            if passed:
                self.tests_passed += 1
                print(f"✓ {test_name}")
            else:
                print(f"✗ {test_name}")
                print(f"  Expected: {expected}")
                print(f"  Got: {result}")
        
        except Exception as e:
            print(f"✗ {test_name}")
            print(f"  Error: {e}")
    
    def summary(self):
        print(f"\n{'=' * 60}")
        print(f"SUMMARY: {self.tests_passed}/{self.tests_run} tests passed")
        percentage = (self.tests_passed / self.tests_run * 100) if self.tests_run > 0 else 0
        print(f"Success Rate: {percentage:.1f}%")
        print('=' * 60)


def test_num_islands():
    runner = TestRunner()
    runner.set_problem("PROBLEM 1: NUMBER OF ISLANDS")
    
    # Test 1: Example case
    grid = [
        ["1","1","0","0","0"],
        ["1","1","0","0","0"],
        ["0","0","1","0","0"],
        ["0","0","0","1","1"]
    ]
    runner.test(num_islands, [row[:] for row in grid], 3, "Test 1: Standard grid with 3 islands")
    
    # Test 2: Single island
    grid = [
        ["1","1","1"],
        ["1","1","1"]
    ]
    runner.test(num_islands, [row[:] for row in grid], 1, "Test 2: Single large island")
    
    # Test 3: All water
    grid = [
        ["0","0","0"],
        ["0","0","0"]
    ]
    runner.test(num_islands, [row[:] for row in grid], 0, "Test 3: All water, no islands")
    
    # Test 4: All land
    grid = [["1"]]
    runner.test(num_islands, [row[:] for row in grid], 1, "Test 4: Single cell land")
    
    # Test 5: Diagonal lands (not connected)
    grid = [
        ["1","0","1"],
        ["0","1","0"],
        ["1","0","1"]
    ]
    runner.test(num_islands, [row[:] for row in grid], 5, "Test 5: Diagonal lands are separate islands")
    
    # Test 6: Snake island
    grid = [
        ["1","0","0"],
        ["1","1","0"],
        ["0","1","1"]
    ]
    runner.test(num_islands, [row[:] for row in grid], 1, "Test 6: Snake-shaped island")
    
    # Test 7: Empty grid
    runner.test(num_islands, [], 0, "Test 7: Empty grid")
    
    # Test 8: Large grid
    grid = [
        ["1","1","0","0","0","1","0"],
        ["1","0","0","0","0","0","0"],
        ["0","0","1","0","1","0","0"],
        ["0","0","0","0","0","1","1"]
    ]
    runner.test(num_islands, [row[:] for row in grid], 5, "Test 8: Larger grid multiple islands")
    
    return runner


def test_clone_graph():
    runner = TestRunner()
    runner.set_problem("PROBLEM 2: CLONE GRAPH")
    
    # Helper to build adjacency list from cloned graph
    def get_adj_list(node, visited=None):
        if not node:
            return []
        if visited is None:
            visited = set()
        if node.val in visited:
            return []
        visited.add(node.val)
        
        adj = {node.val: sorted([n.val for n in node.neighbors])}
        for neighbor in node.neighbors:
            adj.update(get_adj_list(neighbor, visited))
        return adj
    
    # Test 1: Simple 4-node cycle
    node1 = Node(1)
    node2 = Node(2)
    node3 = Node(3)
    node4 = Node(4)
    node1.neighbors = [node2, node4]
    node2.neighbors = [node1, node3]
    node3.neighbors = [node2, node4]
    node4.neighbors = [node1, node3]
    
    cloned = clone_graph(node1)
    runner.tests_run += 1
    if cloned and cloned is not node1 and cloned.val == 1:
        runner.tests_passed += 1
        print("✓ Test 1: Clone created (different object)")
    else:
        print("✗ Test 1: Clone not created properly")
    
    # Test 2: Single node
    node = Node(1)
    cloned = clone_graph(node)
    runner.tests_run += 1
    if cloned and cloned is not node and cloned.val == 1 and len(cloned.neighbors) == 0:
        runner.tests_passed += 1
        print("✓ Test 2: Single node cloned")
    else:
        print("✗ Test 2: Single node clone failed")
    
    # Test 3: Empty graph
    runner.test(clone_graph, None, None, "Test 3: Empty graph (None)")
    
    # Test 4: Two connected nodes
    node1 = Node(1)
    node2 = Node(2)
    node1.neighbors = [node2]
    node2.neighbors = [node1]
    cloned = clone_graph(node1)
    runner.tests_run += 1
    if cloned and len(cloned.neighbors) == 1 and cloned.neighbors[0].val == 2:
        runner.tests_passed += 1
        print("✓ Test 4: Two-node graph cloned")
    else:
        print("✗ Test 4: Two-node graph clone failed")
    
    return runner


def test_pacific_atlantic():
    runner = TestRunner()
    runner.set_problem("PROBLEM 3: PACIFIC ATLANTIC WATER FLOW")
    
    # Test 1: Example case
    heights = [
        [1,2,2,3,5],
        [3,2,3,4,4],
        [2,4,5,3,1],
        [6,7,1,4,5],
        [5,1,1,2,4]
    ]
    expected = [[0,4],[1,3],[1,4],[2,2],[3,0],[3,1],[4,0]]
    runner.test(pacific_atlantic, heights, expected, "Test 1: Standard 5x5 grid")
    
    # Test 2: Single cell
    runner.test(pacific_atlantic, [[1]], [[0,0]], "Test 2: Single cell reaches both oceans")
    
    # Test 3: All same height
    heights = [[5,5],[5,5],[5,5]]
    expected = [[0,0],[0,1],[1,0],[1,1],[2,0],[2,1]]
    runner.test(pacific_atlantic, heights, expected, "Test 3: All same height")
    
    # Test 4: Ascending from Pacific
    heights = [[1,2,3],[4,5,6]]
    expected = []
    runner.test(pacific_atlantic, heights, expected, "Test 4: Only ascending, no cells reach both")
    
    # Test 5: Straight line
    heights = [[1],[2],[3]]
    expected = [[0,0],[1,0],[2,0]]
    runner.test(pacific_atlantic, heights, expected, "Test 5: Single column")
    
    # Test 6: Single row
    heights = [[1,2,3,4,5]]
    expected = [[0,0],[0,1],[0,2],[0,3],[0,4]]
    runner.test(pacific_atlantic, heights, expected, "Test 6: Single row")
    
    # Test 7: Valley in middle
    heights = [
        [10,10,10],
        [10,1,10],
        [10,10,10]
    ]
    expected = [[0,0],[0,1],[0,2],[1,0],[1,2],[2,0],[2,1],[2,2]]
    runner.test(pacific_atlantic, heights, expected, "Test 7: Valley blocks center cell")
    
    return runner


def test_can_finish():
    runner = TestRunner()
    runner.set_problem("PROBLEM 4: COURSE SCHEDULE")
    
    # Test 1: Linear dependency
    runner.test(can_finish, (2, [[1,0]]), True, "Test 1: Simple linear [1,0]")
    
    # Test 2: Circular dependency
    runner.test(can_finish, (2, [[1,0],[0,1]]), False, "Test 2: Cycle [1,0],[0,1]")
    
    # Test 3: No prerequisites
    runner.test(can_finish, (3, []), True, "Test 3: No prerequisites")
    
    # Test 4: Multiple paths, no cycle
    runner.test(can_finish, (4, [[1,0],[2,0],[3,1],[3,2]]), True, "Test 4: DAG with multiple paths")
    
    # Test 5: Self-loop
    runner.test(can_finish, (1, [[0,0]]), False, "Test 5: Self-loop")
    
    # Test 6: Complex cycle
    runner.test(can_finish, (4, [[0,1],[1,2],[2,3],[3,1]]), False, "Test 6: Cycle in chain")
    
    # Test 7: Large course count
    runner.test(can_finish, (100, [[1,0]]), True, "Test 7: Many courses, simple dependency")
    
    # Test 8: Multiple independent components
    runner.test(can_finish, (6, [[1,0],[2,1],[4,3],[5,4]]), True, "Test 8: Two separate chains")
    
    # Test 9: Triangle
    runner.test(can_finish, (3, [[0,1],[1,2],[2,0]]), False, "Test 9: Triangle cycle")
    
    return runner


def test_solve():
    runner = TestRunner()
    runner.set_problem("PROBLEM 5: SURROUNDED REGIONS")
    
    # Test 1: Standard case
    board = [
        ["X","X","X","X"],
        ["X","O","O","X"],
        ["X","X","O","X"],
        ["X","O","X","X"]
    ]
    expected = [
        ["X","X","X","X"],
        ["X","X","X","X"],
        ["X","X","X","X"],
        ["X","O","X","X"]
    ]
    solve(board)
    runner.test(lambda b: b, board, expected, "Test 1: Standard board with border O")
    
    # Test 2: All X's
    board = [["X","X"],["X","X"]]
    expected = [["X","X"],["X","X"]]
    solve(board)
    runner.test(lambda b: b, board, expected, "Test 2: All X's, no change")
    
    # Test 3: Border O's
    board = [
        ["O","X","O"],
        ["X","O","X"],
        ["O","X","O"]
    ]
    expected = [
        ["O","X","O"],
        ["X","X","X"],
        ["O","X","O"]
    ]
    solve(board)
    runner.test(lambda b: b, board, expected, "Test 3: Border O's protected, center captured")
    
    # Test 4: Single cell
    board = [["O"]]
    expected = [["O"]]
    solve(board)
    runner.test(lambda b: b, board, expected, "Test 4: Single O on border")
    
    # Test 5: All O's
    board = [["O","O"],["O","O"]]
    expected = [["O","O"],["O","O"]]
    solve(board)
    runner.test(lambda b: b, board, expected, "Test 5: All O's on border, no capture")
    
    # Test 6: Complex connected
    board = [
        ["X","O","X","X"],
        ["O","X","O","X"],
        ["X","O","X","O"],
        ["O","X","O","X"]
    ]
    expected = [
        ["X","O","X","X"],
        ["O","X","X","X"],
        ["X","X","X","O"],
        ["O","X","O","X"]
    ]
    solve(board)
    runner.test(lambda b: b, board, expected, "Test 6: Complex pattern")
    
    return runner


def test_oranges_rotting():
    runner = TestRunner()
    runner.set_problem("PROBLEM 6: ROTTING ORANGES")
    
    # Test 1: Standard case
    grid = [
        [2,1,1],
        [1,1,0],
        [0,1,1]
    ]
    runner.test(oranges_rotting, grid, 4, "Test 1: Standard grid, 4 minutes")
    
    # Test 2: Already all rotten
    grid = [[2,2],[2,2]]
    runner.test(oranges_rotting, grid, 0, "Test 2: All already rotten")
    
    # Test 3: Impossible to rot
    grid = [[2,1,1],[0,1,1],[1,0,1]]
    runner.test(oranges_rotting, grid, -1, "Test 3: Blocked, cannot rot all")
    
    # Test 4: No fresh oranges
    grid = [[0,2,0],[0,0,0]]
    runner.test(oranges_rotting, grid, 0, "Test 4: No fresh oranges")
    
    # Test 5: Single rotten spreads
    grid = [
        [2,1,1],
        [1,1,1],
        [1,1,1]
    ]
    runner.test(oranges_rotting, grid, 4, "Test 5: Single rotten spreads to all")
    
    # Test 6: Multiple rotten sources
    grid = [
        [2,1,1],
        [1,1,1],
        [1,1,2]
    ]
    runner.test(oranges_rotting, grid, 2, "Test 6: Two rotten sources converge")
    
    # Test 7: Only fresh (impossible)
    grid = [[1,1],[1,1]]
    runner.test(oranges_rotting, grid, -1, "Test 7: No rotten oranges, impossible")
    
    # Test 8: Empty grid
    grid = [[0]]
    runner.test(oranges_rotting, grid, 0, "Test 8: Empty cell")
    
    # Test 9: Linear spread
    grid = [[2,1,1,1,1]]
    runner.test(oranges_rotting, grid, 4, "Test 9: Linear spread")
    
    # Test 10: Cross pattern
    grid = [
        [0,1,0],
        [1,2,1],
        [0,1,0]
    ]
    runner.test(oranges_rotting, grid, 1, "Test 10: Cross pattern, 1 minute")
    
    return runner


if __name__ == "__main__":
    print("\n" + "=" * 60)
    print("GRAPH BFS & DFS - TEST SUITE")
    print("=" * 60)
    
    all_runners = []
    
    # Run all tests
    all_runners.append(test_num_islands())
    all_runners.append(test_clone_graph())
    all_runners.append(test_pacific_atlantic())
    all_runners.append(test_can_finish())
    all_runners.append(test_solve())
    all_runners.append(test_oranges_rotting())
    
    # Overall summary
    total_tests = sum(r.tests_run for r in all_runners)
    total_passed = sum(r.tests_passed for r in all_runners)
    
    print("\n" + "=" * 60)
    print("OVERALL SUMMARY")
    print("=" * 60)
    print(f"Total Tests: {total_tests}")
    print(f"Passed: {total_passed}")
    print(f"Failed: {total_tests - total_passed}")
    percentage = (total_passed / total_tests * 100) if total_tests > 0 else 0
    print(f"Success Rate: {percentage:.1f}%")
    print("=" * 60)
    
    # Grade
    if percentage >= 95:
        grade = "A+"
    elif percentage >= 90:
        grade = "A"
    elif percentage >= 85:
        grade = "B+"
    elif percentage >= 80:
        grade = "B"
    elif percentage >= 75:
        grade = "C+"
    elif percentage >= 70:
        grade = "C"
    else:
        grade = "D"
    
    print(f"\nGrade: {grade}")
    print("=" * 60)
