class Solution:
    def integerBreak(self, n: int) -> int:
        # Handle base cases
        if n == 2:
            return 1
        if n == 3:
            return 2

        # Dynamic programming table to store maximum products
        max_product = [0] * (n + 1)

        # Base cases for numbers 1, 2, and 3 -only for computing for the rest of the numbers-
        max_product[1] = 1
        max_product[2] = 2
        max_product[3] = 3

        # Fill the dynamic programming table for larger numbers
        for num in range(4, n + 1):
            max_product_for_num = 0
            # Iterate through smaller numbers to calculate the maximum product
            for sub_num in range(1, num // 2 + 1):
                max_product_for_num = max(max_product_for_num, max_product[sub_num] * max_product[num - sub_num])
            # Update the maximum product for the current number
            max_product[num] = max_product_for_num

        return max_product[n]