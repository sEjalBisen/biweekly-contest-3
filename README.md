# NXT Wave Biweekly Contest #3

Solutions for NXT Wave Biweekly Contest #3 problems.

### Problems Solved:
1. **Product of Digits Sum** - `product_of_digit_sums.py`
   - **Task:** Given two integers A and B, find sum of digits of A and sum of digits of B, then return product of both sums
   - **Approach:** Extract each digit using `num % 10`, add to total, divide num by 10. Do for both A and B
   - **Time Complexity:** O(log A + log B) 
   - **Space Complexity:** O(1)
   - **Difficulty:** Easy

Language: Python  
Platform: NXT Wave