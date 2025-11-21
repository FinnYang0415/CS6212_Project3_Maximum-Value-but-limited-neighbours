def max_value_limited_neighbors(a, k):
    """
    Find the maximum sum by selecting elements from array a,
    with at most k adjacent 1s in the selection array b.
    
    Args:
        a: List of positive numbers
        k: Maximum number of adjacent 1s allowed
        
    Returns:
        tuple: (max_sum, selection_array_b)
    """
    n = len(a)
    if n == 0:
        return 0, []
    
    # dp[i][j][last] = maximum sum considering first i elements,
    # with j adjacent pairs used, and last indicates if a[i-1] is selected (1) or not (0)
    # We use -infinity to represent impossible states
    INF = float('-inf')
    
    # Initialize DP table
    dp = [[[INF for _ in range(2)] for _ in range(k + 2)] for _ in range(n + 1)]
    
    # Base case: no elements considered, no adjacent pairs, last is 0 (nothing selected)
    dp[0][0][0] = 0
    
    # Fill the DP table
    for i in range(1, n + 1):
        for j in range(k + 2):
            # Case 1: Don't select a[i-1] (b[i-1] = 0)
            if dp[i-1][j][0] != INF:
                dp[i][j][0] = max(dp[i][j][0], dp[i-1][j][0])
            if dp[i-1][j][1] != INF:
                dp[i][j][0] = max(dp[i][j][0], dp[i-1][j][1])
            
            # Case 2: Select a[i-1] (b[i-1] = 1)
            # Coming from last=0 (previous element not selected)
            if dp[i-1][j][0] != INF:
                dp[i][j][1] = max(dp[i][j][1], dp[i-1][j][0] + a[i-1])
            
            # Coming from last=1 (previous element selected, creates an adjacent pair)
            if j > 0 and dp[i-1][j-1][1] != INF:
                dp[i][j][1] = max(dp[i][j][1], dp[i-1][j-1][1] + a[i-1])
    
    # Find the maximum value
    max_sum = INF
    best_j = -1
    best_last = -1
    
    for j in range(k + 1):
        for last in range(2):
            if dp[n][j][last] > max_sum:
                max_sum = dp[n][j][last]
                best_j = j
                best_last = last
    
    # Backtrack to find the selection array b
    b = [0] * n
    current_j = best_j
    current_last = best_last
    
    for i in range(n, 0, -1):
        if current_last == 1:
            # a[i-1] is selected
            b[i-1] = 1
            
            # Check where we came from
            if current_j > 0 and dp[i-1][current_j-1][1] != INF:
                if dp[i][current_j][1] == dp[i-1][current_j-1][1] + a[i-1]:
                    # Came from last=1 (adjacent pair created)
                    current_j -= 1
                    current_last = 1
                    continue
            
            # Must have come from last=0
            if dp[i-1][current_j][0] != INF:
                if dp[i][current_j][1] == dp[i-1][current_j][0] + a[i-1]:
                    current_last = 0
                    continue
        else:
            # a[i-1] is not selected
            b[i-1] = 0
            
            # Check where we came from
            if dp[i-1][current_j][1] != INF:
                if dp[i][current_j][0] == dp[i-1][current_j][1]:
                    current_last = 1
                    continue
            
            if dp[i-1][current_j][0] != INF:
                if dp[i][current_j][0] == dp[i-1][current_j][0]:
                    current_last = 0
                    continue
    
    return max_sum, b


def count_adjacent_ones(b):
    """Count the number of adjacent 1s in array b."""
    count = 0
    for i in range(len(b) - 1):
        if b[i] == 1 and b[i+1] == 1:
            count += 1
    return count


def verify_solution(a, b, k):
    """Verify that the solution is valid."""
    # Check that b contains only 0s and 1s
    if not all(x in [0, 1] for x in b):
        return False, "b contains values other than 0 and 1"
    
    # Check that adjacent 1s don't exceed k
    adj_count = count_adjacent_ones(b)
    if adj_count > k:
        return False, f"Adjacent 1s count ({adj_count}) exceeds k ({k})"
    
    # Calculate sum
    total = sum(a[i] * b[i] for i in range(len(a)))
    
    return True, f"Valid solution with sum={total}, adjacent 1s={adj_count}"


# Test cases
if __name__ == "__main__":
    # Test case 1
    a1 = [100, 300, 400, 50]
    k1 = 1
    max_sum1, b1 = max_value_limited_neighbors(a1, k1)
    print(f"Test 1: a={a1}, k={k1}")
    print(f"Result: b={b1}, sum={max_sum1}")
    print(f"Verification: {verify_solution(a1, b1, k1)}")
    print()
    
    # Test case 2
    a2 = [10, 100, 300, 400, 50, 4500, 200, 30, 90]
    k2 = 2
    max_sum2, b2 = max_value_limited_neighbors(a2, k2)
    print(f"Test 2: a={a2}, k={k2}")
    print(f"Result: b={b2}, sum={max_sum2}")
    print(f"Verification: {verify_solution(a2, b2, k2)}")
    print()
    
    # Test case 3: k=0 (no adjacent 1s allowed)
    a3 = [1, 5, 3, 8, 2]
    k3 = 0
    max_sum3, b3 = max_value_limited_neighbors(a3, k3)
    print(f"Test 3: a={a3}, k={k3}")
    print(f"Result: b={b3}, sum={max_sum3}")
    print(f"Verification: {verify_solution(a3, b3, k3)}")
    print()
    
    # Test case 4: k large (no restriction)
    a4 = [1, 2, 3, 4, 5]
    k4 = 10
    max_sum4, b4 = max_value_limited_neighbors(a4, k4)
    print(f"Test 4: a={a4}, k={k4}")
    print(f"Result: b={b4}, sum={max_sum4}")
    print(f"Verification: {verify_solution(a4, b4, k4)}")
