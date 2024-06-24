def is_word_palindrome(word:str)->str:
    lower_word = word.lower()
    
    if lower_word == lower_word[::-1]:
        return f"Yes, the word '{word}' is a palindrome"
    else:
        return f"No, the word '{word}' is not a palindrome"

# Example usage:
print(is_word_palindrome("Pallindrom"))  
print(is_word_palindrome("madam"))       
print(is_word_palindrome("Level"))   