
from re import sub


def lengthOfLongestSubstring(s: str) -> int:
    substring : str = ""
    max_length : int = 0
    for letter in s:
        if letter not in substring:
            substring += letter
        else:
            if max_length < len(substring):
                max_length = len(substring)
            index_of_found_letter : int = substring.find(letter)
            substring = substring[index_of_found_letter + 1:]
            substring += letter
            
    if max_length < len(substring):
        max_length = len(substring)
    return max_length

s = "aabaab!"
print(lengthOfLongestSubstring(s))
