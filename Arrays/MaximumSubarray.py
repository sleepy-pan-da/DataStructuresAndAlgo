from typing import List

# def maxSubArray(nums: List[int]) -> int:
#     max_sum_from_sub_array : int = nums[0]
#     for starting_index in range(len(nums)):
        
#         current_sum : int = nums[starting_index]
#         if current_sum > max_sum_from_sub_array:
#             max_sum_from_sub_array = current_sum
        
#         for second_index in range(starting_index + 1, len(nums)):
#             current_sum += nums[second_index]
#             if current_sum_from_sub_array > max_sum_from_sub_array:
#                 max_sum_from_sub_array = current_sum_from_sub_array
    
#     return max_sum_from_sub_array

def maxSubArray(nums: List[int]) -> int:
    # sliding window approach
    # when current sum < 0, bring forward the window

    # initialisation
    max_sum : int = nums[0]
    current_sum : int = 0

    for index in range(len(nums)):
        current_sum += nums[index]

        if current_sum > max_sum:
            max_sum = current_sum  

        if current_sum < 0:
            current_sum = 0
    return max_sum


nums : List[int] = [3, -2, 1]
print(maxSubArray(nums))