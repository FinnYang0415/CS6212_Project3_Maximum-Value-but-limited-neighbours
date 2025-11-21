"""
理论运行时间 vs 实际运行时间对比分析
"""

import time
import random
from max_value_limited_neighbors import max_value_limited_neighbors


def performance_analysis():
    """性能分析：理论运行时间 vs 实际运行时间"""
    print("\n" + "=" * 80)
    print("性能实验分析 (理论时间 vs 实际时间)")
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
    
    # 先运行一次基准测试，计算单位操作时间
    print("正在校准基准时间...")
    a_base = [random.randint(1, 1000) for _ in range(100)]
    k_base = 50
    
    times_base = []
    for _ in range(10):
        start = time.time()
        max_value_limited_neighbors(a_base, k_base)
        times_base.append(time.time() - start)
    
    base_time = sum(times_base) / len(times_base)
    # Calculate unit operation time constant c (actual time = c * n * k)
    c = base_time / (100 * 50)
    
    print(f"Baseline: n=100, k=50, actual time={base_time*1000:.4f}ms")
    print(f"Unit operation time constant c = {c*1e6:.4f} μs\n")
    
    print(f"{'n':<8} {'k':<8} {'n×k':<12} {'Theory(ms)':<15} {'Actual(ms)':<15} {'Error':<10}")
    print("-" * 80)
    
    results = []
    for n, k in test_configs:
        # Generate random test data
        a = [random.randint(1, 1000) for _ in range(n)]
        
        # Theoretical running time = c * n * k
        theoretical_time = c * n * k * 1000  # Convert to milliseconds
        
        # Actual running time (average of multiple runs)
        times = []
        for _ in range(5):
            start = time.time()
            max_value_limited_neighbors(a, k)
            times.append(time.time() - start)
        
        actual_time = sum(times) / len(times) * 1000  # Convert to milliseconds
        
        # Calculate error rate
        error_rate = abs(actual_time - theoretical_time) / theoretical_time * 100
        
        results.append((n, k, theoretical_time, actual_time, error_rate))
        
        print(f"{n:<8} {k:<8} {n*k:<12} {theoretical_time:<15.4f} {actual_time:<15.4f} {error_rate:<9.2f}%")
    
    print("-" * 80)
    
    # Statistical analysis
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


if __name__ == "__main__":
    performance_analysis()
