from typing import List

def max_subarray_sum(nums: List[int]) -> int:
    max_sum = float('-inf')
    current_sum = 0

    for num in nums:
        current_sum = max(num, current_sum + num)
        max_sum = max(max_sum, current_sum)

    return max_sum

# Test the function
nums1 = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
nums2 = [1, -2, 3, -4, 5, -6]
print(max_subarray_sum(nums1))  # Output: 6
print(max_subarray_sum(nums2))  # Output: 5
