class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        left_pointer = 1
        right_pointer = len(numbers)

        while left_pointer <= right_pointer:
            if numbers[left_pointer - 1] + numbers[right_pointer - 1] == target:
                return [left_pointer, right_pointer]
            elif numbers[left_pointer - 1] + numbers[right_pointer - 1] > target:
                right_pointer -= 1
            else:
                left_pointer += 1