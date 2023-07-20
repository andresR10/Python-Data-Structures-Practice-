def vowel_count(phrase):
    """Return frequency map of vowels, case-insensitive.

        >>> vowel_count('rithm school')
        {'i': 1, 'o': 2}
        
        >>> vowel_count('HOW ARE YOU? i am great!') 
        {'o': 2, 'a': 3, 'e': 2, 'u': 1, 'i': 1}
    """
    vowels = 'aeiou'
    count = {}


    for char in phrase:
        char_lowered = char.lower()
        if char_lowered in vowels:
            count[char_lowered] = count.get(char_lowered, 0) + 1
    return count 

        
