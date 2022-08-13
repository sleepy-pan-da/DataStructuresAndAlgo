
from curses.ascii import isalnum
from distutils.command.clean import clean


def isPalindrome(s: str) -> bool:
    # clean string by removing non-alphanumeric
    cleaned_string : str = ""
    for letter in s:
        if letter.isalnum():
            cleaned_string += letter
    
    # make everything lowercase
    cleaned_string = cleaned_string.lower()
    reversed_string : str = cleaned_string[::-1]
    return reversed_string == cleaned_string

s = "race a car"
print(isPalindrome(s))