import unittest
from max_value_limited_neighbors import (
    max_value_limited_neighbors,
    count_adjacent_ones,
    verify_solution
)


class TestMaxValueLimitedNeighbors(unittest.TestCase):
    
    def test_example_1(self):
        """Test case 1 from problem description"""
        a = [100, 300, 400, 50]
        k = 1
        max_sum, b = max_value_limited_neighbors(a, k)
        
        self.assertEqual(max_sum, 700)
        self.assertEqual(b, [0, 1, 1, 0])
        self.assertTrue(verify_solution(a, b, k)[0])
        self.assertLessEqual(count_adjacent_ones(b), k)
    
    def test_example_2(self):
        """Test case 2 from problem description"""
        a = [10, 100, 300, 400, 50, 4500, 200, 30, 90]
        k = 2
        max_sum, b = max_value_limited_neighbors(a, k)
        
        self.assertEqual(max_sum, 5500)
        self.assertEqual(b, [1, 0, 1, 1, 0, 1, 1, 0, 1])
        self.assertTrue(verify_solution(a, b, k)[0])
        self.assertLessEqual(count_adjacent_ones(b), k)
    
    def test_k_zero_no_adjacent_allowed(self):
        """Test with k=0 (no adjacent 1s allowed)"""
        a = [1, 5, 3, 8, 2]
        k = 0
        max_sum, b = max_value_limited_neighbors(a, k)
        
        self.assertEqual(max_sum, 13)  # 5 + 8 = 13
        self.assertEqual(count_adjacent_ones(b), 0)
        self.assertTrue(verify_solution(a, b, k)[0])
    
    def test_k_large_select_all(self):
        """Test with large k (can select all elements)"""
        a = [1, 2, 3, 4, 5]
        k = 10
        max_sum, b = max_value_limited_neighbors(a, k)
        
        self.assertEqual(max_sum, 15)  # Sum of all
        self.assertEqual(b, [1, 1, 1, 1, 1])
        self.assertTrue(verify_solution(a, b, k)[0])
    
    def test_single_element(self):
        """Test with single element"""
        a = [100]
        k = 0
        max_sum, b = max_value_limited_neighbors(a, k)
        
        self.assertEqual(max_sum, 100)
        self.assertEqual(b, [1])
        self.assertTrue(verify_solution(a, b, k)[0])
    
    def test_two_elements_k_zero(self):
        """Test with two elements and k=0"""
        a = [50, 100]
        k = 0
        max_sum, b = max_value_limited_neighbors(a, k)
        
        self.assertEqual(max_sum, 100)
        self.assertEqual(b, [0, 1])
        self.assertLessEqual(count_adjacent_ones(b), k)
    
    def test_two_elements_k_one(self):
        """Test with two elements and k=1"""
        a = [50, 100]
        k = 1
        max_sum, b = max_value_limited_neighbors(a, k)
        
        self.assertEqual(max_sum, 150)
        self.assertEqual(b, [1, 1])
        self.assertEqual(count_adjacent_ones(b), 1)
    
    def test_alternating_values(self):
        """Test with alternating high and low values"""
        a = [100, 1, 100, 1, 100]
        k = 1
        max_sum, b = max_value_limited_neighbors(a, k)
        
        # Should select the high values optimally
        self.assertGreaterEqual(max_sum, 300)
        self.assertTrue(verify_solution(a, b, k)[0])
        self.assertLessEqual(count_adjacent_ones(b), k)
    
    def test_descending_order(self):
        """Test with descending values"""
        a = [100, 90, 80, 70, 60]
        k = 2
        max_sum, b = max_value_limited_neighbors(a, k)
        
        self.assertTrue(verify_solution(a, b, k)[0])
        self.assertLessEqual(count_adjacent_ones(b), k)
    
    def test_ascending_order(self):
        """Test with ascending values"""
        a = [10, 20, 30, 40, 50]
        k = 1
        max_sum, b = max_value_limited_neighbors(a, k)
        
        # Should prefer the last two elements (40 + 50 = 90)
        self.assertGreaterEqual(max_sum, 90)
        self.assertTrue(verify_solution(a, b, k)[0])
        self.assertLessEqual(count_adjacent_ones(b), k)
    
    def test_all_same_values(self):
        """Test with all same values"""
        a = [10, 10, 10, 10, 10]
        k = 2
        max_sum, b = max_value_limited_neighbors(a, k)
        
        self.assertTrue(verify_solution(a, b, k)[0])
        self.assertLessEqual(count_adjacent_ones(b), k)
        # With k=2, can select at most 4 elements (creating 3 adjacent pairs would exceed k)
        # Actually with k=2, we can select elements with at most 2 adjacent pairs
        self.assertEqual(sum(b), 4)  # e.g., [1,1,1,0,1] has 2 adjacent pairs
    
    def test_empty_array(self):
        """Test with empty array"""
        a = []
        k = 0
        max_sum, b = max_value_limited_neighbors(a, k)
        
        self.assertEqual(max_sum, 0)
        self.assertEqual(b, [])
    
    def test_strategic_selection(self):
        """Test case where strategic selection is needed"""
        a = [1, 100, 1, 100, 1]
        k = 0
        max_sum, b = max_value_limited_neighbors(a, k)
        
        self.assertEqual(max_sum, 200)  # Select both 100s
        self.assertEqual(b, [0, 1, 0, 1, 0])
        self.assertEqual(count_adjacent_ones(b), 0)


class TestCountAdjacentOnes(unittest.TestCase):
    
    def test_no_adjacent(self):
        """Test counting with no adjacent 1s"""
        self.assertEqual(count_adjacent_ones([1, 0, 1, 0, 1]), 0)
        self.assertEqual(count_adjacent_ones([0, 1, 0, 1, 0]), 0)
    
    def test_one_adjacent_pair(self):
        """Test counting with one adjacent pair"""
        self.assertEqual(count_adjacent_ones([0, 1, 1, 0]), 1)
        self.assertEqual(count_adjacent_ones([1, 1, 0, 0]), 1)
    
    def test_multiple_adjacent_pairs(self):
        """Test counting with multiple adjacent pairs"""
        self.assertEqual(count_adjacent_ones([0, 1, 0, 1, 0, 1, 1, 1]), 2)
        self.assertEqual(count_adjacent_ones([0, 1, 0, 0, 1, 1, 1, 1]), 3)
        self.assertEqual(count_adjacent_ones([1, 0, 1, 1, 0, 1, 1, 1]), 3)
    
    def test_all_ones(self):
        """Test counting with all 1s"""
        self.assertEqual(count_adjacent_ones([1, 1, 1, 1]), 3)
    
    def test_all_zeros(self):
        """Test counting with all 0s"""
        self.assertEqual(count_adjacent_ones([0, 0, 0, 0]), 0)
    
    def test_empty(self):
        """Test counting with empty array"""
        self.assertEqual(count_adjacent_ones([]), 0)


class TestVerifySolution(unittest.TestCase):
    
    def test_valid_solution(self):
        """Test verification of valid solution"""
        a = [100, 300, 400, 50]
        b = [0, 1, 1, 0]
        k = 1
        
        is_valid, message = verify_solution(a, b, k)
        self.assertTrue(is_valid)
        self.assertIn("700", message)
    
    def test_invalid_values_in_b(self):
        """Test verification with invalid values in b"""
        a = [100, 300, 400, 50]
        b = [0, 1, 2, 0]
        k = 1
        
        is_valid, message = verify_solution(a, b, k)
        self.assertFalse(is_valid)
        self.assertIn("other than 0 and 1", message)
    
    def test_exceeds_k_limit(self):
        """Test verification when adjacent 1s exceed k"""
        a = [100, 300, 400, 50]
        b = [1, 1, 1, 0]
        k = 1
        
        is_valid, message = verify_solution(a, b, k)
        self.assertFalse(is_valid)
        self.assertIn("exceeds", message)


if __name__ == '__main__':
    unittest.main()
