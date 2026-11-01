def can_construct(ransomNote: str, magazine: str) -> bool:
    """
    Determines if ransomNote can be constructed using letters from magazine.
    Each letter in magazine can only be used once.

    Parameters:
        ransomNote (str): The target string to construct.
        magazine (str): The source string with available characters.

    Returns:
        bool: True if ransomNote can be constructed, False otherwise.
    """
    character_counts = {}
    for character in magazine:
        character_counts[character] = character_counts.get(character, 0) + 1

    for character in ransomNote:
        if character_counts.get(character, 0) == 0:
            return False
        character_counts[character] -= 1

    return True
