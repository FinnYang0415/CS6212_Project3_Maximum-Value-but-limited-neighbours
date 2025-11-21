(base) fan@FandeMacBook-Air project3 % /Users/fan/miniconda/miniconda3/bin/python /Users/fa
n/Documents/project3/max_value_limited_neighbors.py
======================================================================
Basic Test Cases
======================================================================

Test 1: a=[100, 300, 400, 50], k=1
Result: b=[0, 1, 1, 0], sum=700
Verification: (True, 'Valid solution with sum=700, adjacent 1s=1')

Test 2: a=[10, 100, 300, 400, 50, 4500, 200, 30, 90], k=2
Result: b=[1, 0, 1, 1, 0, 1, 1, 0, 1], sum=5500
Verification: (True, 'Valid solution with sum=5500, adjacent 1s=2')

Test 3: a=[1, 5, 3, 8, 2], k=0
Result: b=[0, 1, 0, 1, 0], sum=13
Verification: (True, 'Valid solution with sum=13, adjacent 1s=0')

Test 4: a=[1, 2, 3, 4, 5], k=10
Result: b=[1, 1, 1, 1, 1], sum=15
Verification: (True, 'Valid solution with sum=15, adjacent 1s=4')

================================================================================
Performance Analysis (Theoretical Time vs Actual Time)
================================================================================
Step 1: Running experiments and collecting actual data...
n        k        n×k          Actual(ms)     
--------------------------------------------------
10       5        50           0.0683         
20       10       200          0.2356         
50       25       1250         1.5811         
100      50       5000         5.4234         
200      100      20000        21.9270        
500      250      125000       145.7241       
1000     500      500000       635.5733       

Step 2: Calibrating unit operation time constant c...
Calibration point: n=100, k=50, actual time=5.4234ms
Unit operation time constant c = 1.0847 μs

Step 3: Calculating theoretical times and comparing with experiments...
n        k        n×k          Theory(ms)      Actual(ms)      Error     
--------------------------------------------------------------------------------
10       5        50           0.0542          0.0683          25.99    %
20       10       200          0.2169          0.2356          8.61     %
50       25       1250         1.3559          1.5811          16.62    %
100      50       5000         5.4234          5.4234          0.00     % *
200      100      20000        21.6936         21.9270         1.08     %
500      250      125000       135.5851        145.7241        7.48     %
1000     500      500000       542.3403        635.5733        17.19    %
--------------------------------------------------------------------------------

Error Statistics:
  Average error: 10.99%
  Maximum error: 25.99%
  Minimum error: 0.00%

Complexity Verification:
  Scale grows from n×k=10×5=50 to n×k=1000×500=500000
  Theoretical time growth: 0.0542ms → 542.3403ms (10000.00x)
  Actual time growth: 0.0683ms → 635.5733ms (9301.42x)
  Growth ratio error: 6.99%
  ✓ Conclusion: Actual time closely matches theoretical prediction, confirms O(n×k) complexity
================================================================================

Step 4: Generating comparison plot...
  ✓ Plot saved as 'performance_analysis.png'

================================================================================
Analysis Complete!
================================================================================