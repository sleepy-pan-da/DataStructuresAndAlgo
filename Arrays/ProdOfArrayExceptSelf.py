from typing import List



def productExceptSelf(nums: List[int]) -> List[int]:
    prefix : List[int] = []
    postfix : List[int] = []
    for num in nums:
        prefix.append(1)
        postfix.append(1)

    # compute prefix array
    for index in range(1, len(nums)):
        prefix[index] = prefix[index-1] * nums[index-1]
    
    # compute postfix array
    for index in range(len(nums)-2, -1, -1):
        postfix[index] = postfix[index+1] * nums[index+1]

    result : List[int] = []
    # multiply them together
    for index in range(len(nums)):
        result.append(prefix[index] * postfix[index])
    return result

nums = [1,2,3,4]
print(productExceptSelf(nums))