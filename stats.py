def get_word_count(text):
    words = text.split()
    return len(words)

def character_dict(text):
    # Create a dictionary to store character counts
    char_count = {}
    
    # Iterate through each character in the text
    for char in text:
        # If the character is not a space, add it to the dictionary
        char = char.lower()
        if char != " ":
            if char in char_count:
                char_count[char] += 1
            else:
                char_count[char] = 1
    
    return char_count