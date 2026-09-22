class Solution:
    def minOperations(self, grid, x):
        nums = []

        # Flatten the grid
        for row in grid:
            for val in row:
                nums.append(val)

        # All values must have same remainder modulo x
        rem = nums[0] % x

        for val in nums:
            if val % x != rem:
                return -1

        # Median minimizes total absolute difference
        nums.sort()
        median = nums[len(nums) // 2]

        operations = 0

        for val in nums:
            operations += abs(val - median) // x

        return operations