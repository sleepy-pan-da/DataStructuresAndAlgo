def isAnagram(s: str, t: str) -> bool:
    letter_count_in_string = {}

    for letter in s:
        if letter not in letter_count_in_string:
            letter_count_in_string[letter] = 1
        else:
            letter_count_in_string[letter] += 1
    
    for letter in t:
        if letter not in letter_count_in_string:
            return False
        else:
            letter_count_in_string[letter] -= 1
            if letter_count_in_string[letter] < 0:
                return False

    for letter in letter_count_in_string:
        if letter_count_in_string[letter] > 0:
            return False

    return True

print(isAnagram("anagram", "nagarams"))