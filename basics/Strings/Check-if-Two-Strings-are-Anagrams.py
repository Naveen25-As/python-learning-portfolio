# Check if Two Strings are Anagrams
str1 = input("Enter first string: ")
str2 = input("Enter second string: ")

if sorted(str1.lower()) == sorted(str2.lower()):
    print("Anagrams")
else:
    print("Not Anagrams")