def reverse(s):
    words = s.split()
    reverse = list(reversed(words))
    sentence = " ".join(reverse)
    return sentence
    
input = input("Enter a sentence: ")
print (reverse(input))
