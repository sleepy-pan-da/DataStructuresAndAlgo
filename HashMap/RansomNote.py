from collections import Counter

def canConstruct(ransomNote: str, magazine: str) -> bool:
    characters_from_magazine = {}
    
    for char in magazine:
        if char in characters_from_magazine:
            characters_from_magazine[char] += 1
        else:
            characters_from_magazine[char] = 1

    print(characters_from_magazine)

    for char in ransomNote:
        if char not in characters_from_magazine:
            return False
        else:
            characters_from_magazine[char] -= 1
            if characters_from_magazine[char] == 0:
                characters_from_magazine.pop(char)
    return True

print(canConstruct("aa", "aab"))


print()
char_counter = Counter("mississippi")
print(char_counter)