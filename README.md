# Project 3  
**November 2025**

---

## 1. Problem Statement

We are given a positive integer array \(a[1..n]\) and an integer \(k\).  
We want to construct a binary array \(b[1..n]\), where each \(b[j] \in \{0, 1\}\), such that:

1. The number of adjacent pairs of 1s in \(b\) (i.e., indices \(j\) where \(b[j] = 1\) and \(b[j+1] = 1\)) is **at most** \(k\).  
2. The following sum is maximized:
   \[
   \sum_{j=1}^{n} a[j] \cdot b[j].
   \]

The output of the program is:

- The **maximum value** of the sum.  
- One corresponding binary array **b** that achieves this maximum under the adjacency constraint.

---

## 2. Theoretical Analysis

A naive brute-force approach would enumerate all \(2^n\) possible binary arrays \(b\), check the number of adjacent 1s for each, and keep the best valid sum.  
This is clearly infeasible for large \(n\).

The key difficulty is that the contribution of choosing position \(i\) (setting \(b[i] = 1\)) depends on whether the previous position \(i-1\) was also chosen, because that may create an additional adjacent pair of 1s.  
Therefore, a **dynamic programming** solution is appropriate.

### 2.1 DP State Definition

We define a 3D DP table:

\[
dp[i][j][t]
\]

where:

- \(i\) : we have considered the first \(i\) elements (positions 1..i).  
- \(j\) : we have used exactly \(j\) adjacent 1-pairs among these \(i\) positions.  
- \(t\) : the value of \(b[i]\):
  - \(t = 0\) means \(b[i] = 0\).  
  - \(t = 1\) means \(b[i] = 1\).  

The value stored in \(dp[i][j][t]\) is the **maximum sum** we can obtain for positions 1..i under these conditions.  
If a state is impossible, we store a very negative number.

We use the base condition:

- \(dp[0][0][0] = 0\): no elements taken, no adjacency, and we conceptually treat “previous” as 0.  
- All other states for \(i = 0\) are initialized to \(-\infty\).

### 2.2 Transition

For each position \(i\) (1-based) and each possible adjacency count \(j\) (0..k), we consider two choices.

#### Case 1: Set \(b[i] = 0\)

If the current bit is 0, we do not add any value and do not create new adjacencies.  
We can come from either \(b[i-1] = 0\) or \(b[i-1] = 1\) with the same \(j\):

\[
dp[i][j][0] = \max\bigl(dp[i-1][j][0],\ dp[i-1][j][1]\bigr).
\]

#### Case 2: Set \(b[i] = 1\)

If we set the current bit to 1, we add \(a[i]\) to the sum.  
There are two subcases:

1. **Previous bit was 0**: \(b[i-1] = 0\).  
   No new adjacency is created, so \(j\) does not change:
   \[
   dp[i][j][1] = dp[i-1][j][0] + a[i].
   \]

2. **Previous bit was 1**: \(b[i-1] = 1\).  
   This creates one new adjacent pair of 1s, so we must increase the adjacency count by 1:
   \[
   dp[i][j][1] = dp[i-1][j-1][1] + a[i], \quad j > 0.
   \]

For each \(i, j\), we take the maximum value from the valid transitions above.

### 2.3 Result and Backtracking

At the end (when \(i = n\)), the answer is the maximum among:

\[
\max_{0 \leq j \leq k,\ t \in \{0,1\}} dp[n][j][t].
\]

To reconstruct a valid optimal array \(b\), we store parent pointers during the DP transitions and **backtrack** from the best terminal state back to \(i = 1\), recovering the chosen \(b[i]\) at each step.

### 2.4 Time and Space Complexity

- The indices are:  
  - \(i = 0..n\)  
  - \(j = 0..k\)  
  - \(t = 0,1\)

- There are therefore \(O(n \cdot k \cdot 2) = O(nk)\) states.  
- Each state is updated in constant time from at most two previous states.

So:

- **Time Complexity**: \(O(nk)\)  
- **Space Complexity**: \(O(nk)\), which could be optimized to \(O(k)\) if only the current and previous rows in \(i\) are stored.

---

## 3. Experimental Analysis

In this project, experiments mainly serve to **verify correctness** of the DP implementation, rather than to study empirical asymptotic behavior.

### 3.1 Program Listing

The core of the program is a Python function:

```python
def max_value_with_limited_neighbors(a, k):
    # a: list of positive integers
    # k: maximum allowed number of adjacent 1-pairs
    # returns: (best_value, best_b_list)
    ...
```

This function builds the \(dp[i][j][t]\) table, performs backtracking to reconstruct an optimal \(b\), and returns both the maximum sum and the chosen binary array.

### 3.2 Sample Test Cases

We tested the implementation on several inputs, including the examples from the project description.

**Test Case 1**

- Input:  
  - \(a = [100, 300, 400, 50]\)  
  - \(k = 1\)
- Output:  
  - \(b = [0, 1, 1, 0]\)  
  - sum = 700  
- Explanation:  
  The best solution selects the 300 and 400, forming exactly one adjacency between them, which is allowed.

---

**Test Case 2**

- Input:  
  - \(a = [10, 100, 300, 400, 50, 4500, 200, 30, 90]\)  
  - \(k = 2\)
- One optimal output (from the DP):  
  - \(b = [1, 0, 1, 1, 0, 1, 1, 0, 1]\)  
  - sum = 5500  
- Explanation:  
  The selected elements are 10, 300, 400, 4500, 200, 90.  
  There are exactly 2 adjacent 1-pairs, which satisfies the constraint \(k = 2\).

These tests confirm that the implementation both respects the adjacency limit and achieves the maximum sum under that constraint.

---

## 4. Conclusions

In this project, we solved the **Maximum Value with Limited Neighbors** problem using a carefully designed dynamic programming approach.

- The DP state \(dp[i][j][t]\) explicitly tracks how many adjacent 1-pairs have been used and whether the current position is selected.  
- The transitions distinguish between continuing a run of 1s (which consumes one adjacency) and starting a new isolated 1.  
- The algorithm runs in **\(O(nk)\)** time and correctly reconstructs one optimal binary array \(b\).

Theoretical analysis and multiple test cases together support the correctness and efficiency of the solution.
