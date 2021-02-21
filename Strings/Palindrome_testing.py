# 5.9 (Palindrome Tester) A string that’s spelled identically backward and forward, like
# 'radar', is a palindrome. Write a function is_palindrome that takes a string and returns
# True if it’s a palindrome and False otherwise. Use a stack (simulated with a list as we did
# in Section 5.11) to help determine whether a string is a palindrome. Your function should
# ignore case sensitivity (that is, 'a' and 'A' are the same), spaces and punctuation.

client_word = input("Enter a word: ")
new_client_word = client_word[::-1]

if client_word == new_client_word:
    print("the word is a palindrome")
else:
    print("the word is not a palindrome")
