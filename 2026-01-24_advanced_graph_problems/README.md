# Day 24: Advanced Graph Problems

## Goal
Master advanced graph concepts that frequently appear in hard interview rounds and competitive programming.

## Problems
1. **Reconstruct Itinerary** (LeetCode #332)
   - Concept: Eulerian Path (Hierholzer's Algorithm)
   - Pattern: DFS with post-order traversal and reversal.
2. **Is Graph Bipartite?** (LeetCode #785)
   - Concept: Graph Coloring
   - Pattern: BFS/DFS to alternate colors. If a neighbor has the same color, it's not bipartite.
3. **Word Ladder** (LeetCode #127)
   - Concept: Shortest Path in Unweighted Graph
   - Pattern: Bidirectional BFS (or standard BFS) with word transformations.
4. **Critical Connections in a Network** (LeetCode #1192)
   - Concept: Bridge Finding in a Network
   - Pattern: Tarjan's Algorithm (Discovery and Lowest Reached Time tracking).

## Notes
- These algorithms are very specific. Knowing the pattern (e.g., Tarjan's for bridges, Hierholzer's for Eulerian paths) is often required.
- Always check for unconnected components (like in bipartite graph checks).
