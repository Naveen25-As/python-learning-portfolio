# Count Vowels.

def Count_vowels(string):
    vowels = "aeiouAEIOU"
    count = 0
    
    for char in string:
        if char in vowels:
            count += 1
            
    return count

text = input("Enter a string: ")
vowel_count = Count_vowels(text)
print(f"The number of vowels in the string is: {vowel_count}")