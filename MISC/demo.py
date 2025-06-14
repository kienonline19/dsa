def alternating_array_backtrack(nums):
    """
    Create an alternating ascending/descending array using backtracking.
    Pattern: nums[0] < nums[1] > nums[2] < nums[3] > nums[4] < ...
    """
    if len(nums) <= 1:
        return [nums[:]]

    nums.sort()  # Sort to handle duplicates efficiently
    result = []
    used = [False] * len(nums)
    current = []

    def backtrack():
        if len(current) == len(nums):
            result.append(current[:])
            return

        prev_num = None  # Skip duplicates at same position
        for i in range(len(nums)):
            if used[i] or nums[i] == prev_num:
                continue

            # Check alternating pattern
            if len(current) >= 1:
                pos = len(current)
                if pos % 2 == 1:  # Odd position: should be > previous
                    if nums[i] <= current[-1]:
                        continue
                else:  # Even position: should be < previous
                    if nums[i] >= current[-1]:
                        continue

            # Valid choice
            current.append(nums[i])
            used[i] = True
            prev_num = nums[i]

            backtrack()

            # Backtrack
            current.pop()
            used[i] = False

    backtrack()
    return result


def find_all_alternating_arrays(nums):
    """Find all possible alternating arrays"""
    return alternating_array_backtrack(nums)


def find_one_alternating_array(nums):
    """Find just one valid alternating array (more efficient)"""
    if len(nums) <= 1:
        return nums[:]

    nums.sort()
    used = [False] * len(nums)
    result = []

    def backtrack():
        if len(result) == len(nums):
            return True

        prev_num = None
        for i in range(len(nums)):
            if used[i] or nums[i] == prev_num:
                continue

            # Check alternating pattern
            if len(result) >= 1:
                pos = len(result)
                if pos % 2 == 1:  # Should be > previous
                    if nums[i] <= result[-1]:
                        continue
                else:  # Should be < previous
                    if nums[i] >= result[-1]:
                        continue

            result.append(nums[i])
            used[i] = True
            prev_num = nums[i]

            if backtrack():
                return True

            # Backtrack
            result.pop()
            used[i] = False

        return False

    if backtrack():
        return result
    return []


# Example usage and testing
if __name__ == "__main__":
    # Test cases
    test_cases = [[1, 2, 3, 4], [1, 1, 2, 2], [3, 1, 4, 1, 5], [1, 2, 1, 3, 1], [5, 4, 3, 2, 1],
                  [1, 1, 1, 2, 2, 2], [1, 2, 2, 3, 3, 4, 5, 5, 5, 6, 6, 7],
                  [1, 2, 3, 4, 4, 4, 5, 5, 6, 7, 8], [5, 1, 5, 5, 5]]

    for nums in test_cases:
        print(f"\nOriginal: {nums}")

        # Find one solution (faster)
        one_solution = find_one_alternating_array(nums)
        print(f"One solution: {one_solution}")

        # Find all solutions (slower for larger inputs)
        if len(nums) <= 6:  # Only for small inputs
            all_solutions = find_all_alternating_arrays(nums)
            print(f"All solutions ({len(all_solutions)}): {all_solutions}")

        # Verify the pattern
        if one_solution:
            valid = True
            for i in range(1, len(one_solution)):
                if i % 2 == 1:  # Odd index: should be > previous
                    if one_solution[i] <= one_solution[i - 1]:
                        valid = False
                        break
                else:  # Even index: should be < previous
                    if one_solution[i] >= one_solution[i - 1]:
                        valid = False
                        break
            print(f"Valid alternating pattern: {valid}")
