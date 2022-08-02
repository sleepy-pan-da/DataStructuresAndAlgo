from typing import List

# Bruteforce way
# O(n^2)
def twoSum(nums: List[int], target: int) -> List[int]:
    for first_num_index in range(len(nums)):
        for second_num_index in range(first_num_index + 1, len(nums)):
            if nums[first_num_index] + nums[second_num_index] == target:
                return [first_num_index, second_num_index]

# O(n)
# have to use dictionary, which is O(n) in space complexity
def twoSumComplement(nums: List[int], target: int) -> List[int]:
    complements = {}
    for index in range(len(nums)):
        current_num : int = nums[index]
        if current_num in complements:
            return [complements[current_num], index]
        complement : int = target - nums[index]
        complements[complement] = index


nums : List[int] = [2, 7, 11, 15]
target : int = 18

print(twoSum(nums, target))
print(twoSumComplement(nums, target))
