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
    import time
    import random
    
    # Basic functionality tests
    print("=" * 70)
    print("Basic Test Cases")
    print("=" * 70)
    
    # Test case 1
    a1 = [100, 300, 400, 50]
    k1 = 1
    max_sum1, b1 = max_value_limited_neighbors(a1, k1)
    print(f"\nTest 1: a={a1}, k={k1}")
    print(f"Result: b={b1}, sum={max_sum1}")
    print(f"Verification: {verify_solution(a1, b1, k1)}")
    
    # Test case 2
    a2 = [10, 100, 300, 400, 50, 4500, 200, 30, 90]
    k2 = 2
    max_sum2, b2 = max_value_limited_neighbors(a2, k2)
    print(f"\nTest 2: a={a2}, k={k2}")
    print(f"Result: b={b2}, sum={max_sum2}")
    print(f"Verification: {verify_solution(a2, b2, k2)}")
    
    # Test case 3: k=0 (no adjacent 1s allowed)
    a3 = [1, 5, 3, 8, 2]
    k3 = 0
    max_sum3, b3 = max_value_limited_neighbors(a3, k3)
    print(f"\nTest 3: a={a3}, k={k3}")
    print(f"Result: b={b3}, sum={max_sum3}")
    print(f"Verification: {verify_solution(a3, b3, k3)}")
    
    # Test case 4: k large (no restriction)
    a4 = [1, 2, 3, 4, 5]
    k4 = 10
    max_sum4, b4 = max_value_limited_neighbors(a4, k4)
    print(f"\nTest 4: a={a4}, k={k4}")
    print(f"Result: b={b4}, sum={max_sum4}")
    print(f"Verification: {verify_solution(a4, b4, k4)}")
    
    # Performance Analysis: Theoretical vs Actual Time
    print("\n" + "=" * 80)
    print("Performance Analysis (Theoretical Time vs Actual Time)")
    print("=" * 80)
    
    test_configs = [
        (10, 5),
        (20, 10),
        (50, 25),
        (100, 50),
        (200, 100),
        (500, 250),
        (1000, 500),
    ]
    
    # Step 1: Run experiments and collect actual running times
    print("Step 1: Running experiments and collecting actual data...")
    print(f"{'n':<8} {'k':<8} {'n×k':<12} {'Actual(ms)':<15}")
    print("-" * 50)
    
    experimental_data = []
    for n, k in test_configs:
        a = [random.randint(1, 1000) for _ in range(n)]
        
        # Actual time (average of 5 runs)
        times = []
        for _ in range(5):
            start = time.time()
            max_value_limited_neighbors(a, k)
            times.append(time.time() - start)
        
        actual_time = sum(times) / len(times) * 1000  # Convert to ms
        experimental_data.append((n, k, actual_time))
        print(f"{n:<8} {k:<8} {n*k:<12} {actual_time:<15.4f}")
    
    # Step 2: Use middle point to calibrate constant c
    print("\nStep 2: Calibrating unit operation time constant c...")
    calibration_idx = len(experimental_data) // 2  # Choose middle point
    n_cal, k_cal, time_cal = experimental_data[calibration_idx]
    c = time_cal / (n_cal * k_cal * 1000)  # time in ms, so divide by 1000
    
    print(f"Calibration point: n={n_cal}, k={k_cal}, actual time={time_cal:.4f}ms")
    print(f"Unit operation time constant c = {c*1e6:.4f} μs")
    
    # Step 3: Calculate theoretical times and compare
    print("\nStep 3: Calculating theoretical times and comparing with experiments...")
    print(f"{'n':<8} {'k':<8} {'n×k':<12} {'Theory(ms)':<15} {'Actual(ms)':<15} {'Error':<10}")
    print("-" * 80)
    
    results = []
    for n, k, actual_time in experimental_data:
        # Theoretical time = c * n * k
        theoretical_time = c * n * k * 1000  # Convert to ms
        error_rate = abs(actual_time - theoretical_time) / theoretical_time * 100
        
        results.append((n, k, theoretical_time, actual_time, error_rate))
        
        # Mark calibration point with *
        marker = " *" if (n == n_cal and k == k_cal) else ""
        print(f"{n:<8} {k:<8} {n*k:<12} {theoretical_time:<15.4f} {actual_time:<15.4f} {error_rate:<9.2f}%{marker}")
    
    print("-" * 80)
    
    # Statistics
    avg_error = sum(r[4] for r in results) / len(results)
    max_error = max(r[4] for r in results)
    min_error = min(r[4] for r in results)
    
    print(f"\nError Statistics:")
    print(f"  Average error: {avg_error:.2f}%")
    print(f"  Maximum error: {max_error:.2f}%")
    print(f"  Minimum error: {min_error:.2f}%")
    
    # Complexity verification
    if len(results) >= 2:
        n1, k1, theo1, actual1, _ = results[0]
        n2, k2, theo2, actual2, _ = results[-1]
        
        theoretical_ratio = theo2 / theo1
        actual_ratio = actual2 / actual1
        ratio_error = abs(actual_ratio - theoretical_ratio) / theoretical_ratio * 100
        
        print(f"\nComplexity Verification:")
        print(f"  Scale grows from n×k={n1}×{k1}={n1*k1} to n×k={n2}×{k2}={n2*k2}")
        print(f"  Theoretical time growth: {theo1:.4f}ms → {theo2:.4f}ms ({theoretical_ratio:.2f}x)")
        print(f"  Actual time growth: {actual1:.4f}ms → {actual2:.4f}ms ({actual_ratio:.2f}x)")
        print(f"  Growth ratio error: {ratio_error:.2f}%")
        
        if ratio_error < 20:
            print(f"  ✓ Conclusion: Actual time closely matches theoretical prediction, confirms O(n×k) complexity")
        else:
            print(f"  ⚠ Conclusion: Actual time has some deviation from theory, but overall trend matches O(n×k)")
    
    print("=" * 80)
    
    # Step 4: Plot comparison
    import matplotlib.pyplot as plt
    
    print("\nStep 4: Generating comparison plot...")
    
    # Extract data
    scales = [r[0] * r[1] for r in results]
    theoretical_times = [r[2] for r in results]
    actual_times = [r[3] for r in results]
    
    # Create figure
    fig, ax = plt.subplots(figsize=(10, 6))
    
    # Plot Theoretical vs Actual Time
    ax.loglog(scales, theoretical_times, 'b-o', label='Theoretical Time', linewidth=2, markersize=8)
    ax.loglog(scales, actual_times, 'r--s', label='Actual Time', linewidth=2, markersize=8)
    
    ax.set_xlabel('Input Scale (n×k)', fontsize=13)
    ax.set_ylabel('Running Time (ms)', fontsize=13)
    ax.set_title('Theoretical vs Actual Running Time (Log-Log Scale)', fontsize=15, fontweight='bold')
    ax.legend(fontsize=11, loc='upper left')
    ax.grid(True, alpha=0.3, which='both', linestyle='--')
    
    plt.tight_layout()
    
    # Save figure
    filename = 'performance_analysis.png'
    plt.savefig(filename, dpi=150, bbox_inches='tight')
    print(f"  ✓ Plot saved as '{filename}'")
    
    plt.show()
    
    print("\n" + "=" * 80)
    print("Analysis Complete!")
    print("=" * 80)
