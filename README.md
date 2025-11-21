# Maximum Value But Limited Neighbors - Solution Explanation

## Problem Summary
Given an array `a[1..n]` of positive numbers and an integer `k`, find a binary array `b[1..n]` that:
1. Each `b[j]` is either 0 or 1
2. Array `b` has at most `k` adjacent pairs of 1s
3. Maximizes the sum: `sum(a[j] * b[j])`

## Algorithm Approach: Dynamic Programming

### State Definition
We use a 3D DP table: `dp[i][j][last]`

- `i`: Number of elements considered (0 to n)
- `j`: Number of adjacent pairs of 1s used (0 to k)
- `last`: Whether the previous element was selected (0 or 1)
- Value: Maximum sum achievable

### Transitions

For each position `i`, we have two choices:

1. **Don't select `a[i-1]`** (set `b[i-1] = 0`):
   - Can come from any previous state: `dp[i-1][j][0]` or `dp[i-1][j][1]`
   - New state: `dp[i][j][0]`
   - No value added, no adjacent pair created

2. **Select `a[i-1]`** (set `b[i-1] = 1`):
   - If previous was not selected: `dp[i-1][j][0]` → `dp[i][j][1]`
     - Add `a[i-1]` to sum, no adjacent pair created
   - If previous was selected: `dp[i-1][j-1][1]` → `dp[i][j][1]`
     - Add `a[i-1]` to sum, creates one adjacent pair (use one count from `k`)

### Time Complexity
- **Time**: O(n × k)
- **Space**: O(n × k)

### Backtracking
After computing the DP table, we backtrack from `dp[n][best_j][best_last]` to reconstruct the selection array `b`.

## Test Results

### Test Case 1
- Input: `a = [100, 300, 400, 50], k = 1`
- Output: `b = [0, 1, 1, 0], sum = 700`
- Adjacent 1s: 1 (at positions 1-2)
- ✓ Correct!

### Test Case 2
- Input: `a = [10, 100, 300, 400, 50, 4500, 200, 30, 90], k = 2`
- Output: `b = [1, 0, 1, 1, 0, 1, 1, 0, 1], sum = 5500`
- Adjacent 1s: 2 (at positions 2-3 and 5-6)
- Selected values: 10 + 300 + 400 + 4500 + 200 + 90 = 5500
- ✓ Correct!

### Test Case 3 (Edge Case: k=0)
- Input: `a = [1, 5, 3, 8, 2], k = 0`
- Output: `b = [0, 1, 0, 1, 0], sum = 13`
- No adjacent 1s allowed, so we pick alternating maximum values
- ✓ Correct!

### Test Case 4 (No Restriction)
- Input: `a = [1, 2, 3, 4, 5], k = 10`
- Output: `b = [1, 1, 1, 1, 1], sum = 15`
- k is large enough, so we can select all elements
- ✓ Correct!

## Key Insights

1. **Adjacent Pair Definition**: An adjacent pair is formed when two consecutive positions both have 1s. The sequence `[1, 1, 1]` has 2 adjacent pairs.

2. **Greedy vs DP**: A greedy approach won't work because selecting a high-value element might create adjacent pairs that prevent selecting other valuable elements.

3. **State Space**: Tracking the "last" state (whether previous element was selected) is crucial for knowing when we create an adjacent pair.

4. **Optimization**: The algorithm efficiently explores all valid combinations without enumerating all 2^n possibilities.
