# Maximum Value But Limited Neighbors

## Problem Description

Given an array `a[1..n]` of positive numbers and an integer `k`, produce an array `b[1..n]` such that:

1. For each `j`, `b[j]` is 0 or 1
2. Array `b` has adjacent 1s at most `k` times
3. `sum_{j=1 to n} a[j] * b[j]` is maximized

### Examples

**Example 1:**
```
Input:  a = [100, 300, 400, 50], k = 1
Output: b = [0, 1, 1, 0]
Sum:    300 + 400 = 700
```

**Example 2:**
```
Input:  a = [10, 100, 300, 400, 50, 4500, 200, 30, 90], k = 2
Output: b = [1, 0, 1, 1, 0, 1, 1, 0, 1]
Sum:    10 + 300 + 400 + 4500 + 200 + 90 = 5500
```

### Adjacent Pairs Definition

The number of adjacent 1s is counted as consecutive pairs:
- `[0, 1, 0, 1, 0, 1, 1, 1]` has **2** adjacent pairs (one at positions 5-6, one at 6-7)
- `[0, 1, 0, 0, 1, 1, 1, 1]` has **3** adjacent pairs
- `[1, 0, 1, 1, 0, 1, 1, 1]` has **3** adjacent pairs

## Solution Approach

### Dynamic Programming

**State Definition:**
```
dp[i][j][last] = maximum sum considering first i elements,
                 with j adjacent pairs used,
                 last ∈ {0,1} indicates if element i is selected
```

**State Transitions:**

For each position `i`:

1. **Don't select `a[i-1]`:**
   ```
   dp[i][j][0] = max(dp[i-1][j][0], dp[i-1][j][1])
   ```

2. **Select `a[i-1]`:**
   - From `last=0`: `dp[i][j][1] = dp[i-1][j][0] + a[i-1]` (no adjacent pair)
   - From `last=1`: `dp[i][j][1] = dp[i-1][j-1][1] + a[i-1]` (creates adjacent pair)

**Complexity:**
- Time: O(n × k)
- Space: O(n × k)

## Usage

```python
from max_value_limited_neighbors import max_value_limited_neighbors

# Example usage
a = [100, 300, 400, 50]
k = 1
max_sum, b = max_value_limited_neighbors(a, k)

print(f"Selection: {b}")      # [0, 1, 1, 0]
print(f"Maximum sum: {max_sum}")  # 700
```

## Running Tests

```bash
# Run all unit tests
python -m unittest test_max_value_limited_neighbors -v

# Run the example cases
python max_value_limited_neighbors.py
```

## Files

- `max_value_limited_neighbors.py` - Main algorithm implementation
- `test_max_value_limited_neighbors.py` - Comprehensive unit tests (22 test cases)
- `README.md` - Documentation

## Algorithm Features

- Guarantees global optimal solution
- Handles all edge cases (k=0, k>n, empty arrays)
- Efficient O(n*k) time complexity
- Includes solution verification and backtracking
- Full test coverage with 22 unit tests
