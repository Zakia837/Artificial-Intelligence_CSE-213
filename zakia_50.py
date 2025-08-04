# -*- coding: utf-8 -*-
"""
Created on Mon Aug  4 08:22:36 2025

@author: Lab411_07
"""
#1.vowel and consonant
def count_vowels_consonants(name):
    vowels = 'aeiouAEIOU'
    vowel_count = 0
    consonant_count = 0

    for char in name:
        if char.isalpha():  
            if char in vowels:
                vowel_count += 1
            else:
                consonant_count += 1

    print("Full Name:", name)
    print("Number of vowels:", vowel_count)
    print("Number of consonants:", consonant_count)


count_vowels_consonants("Zakia Sultana Chadni")

#2.ASCII value
def display_ascii_values(name):
    print(f"ASCII values for each character in '{name}':")
    for char in name:
        print(f"'{char}' : {ord(char)}")


display_ascii_values("Zakia Sultana Chadni")

#3.Reversed version
def reverse_name(name):
    reversed_name = name[::-1]
    print("Original Name:", name)
    print("Reversed Name:", reversed_name)


reverse_name("Zakia Sultana Chadni")

#4.Palindrome
def is_palindrome(name):
    
    processed_name = ''.join(char.lower() for char in name if char.isalpha())
    reversed_name = processed_name[::-1]

    print("Processed Name:", processed_name)
    print("Reversed Name :", reversed_name)

    if processed_name == reversed_name:
        print("Result: The name is a palindrome.")
    else:
        print("Result: The name is NOT a palindrome.")


is_palindrome("Zakia Sultana Chadni")

#5.List and sort
def get_sorted_unique_letters(name):
    
    letters = [char.lower() for char in name if char.isalpha()]
    unique_letters = sorted(set(letters))  # remove duplicates and sort

    print("Unique letters in alphabetical order:")
    print(unique_letters)


get_sorted_unique_letters("Zakia Sultana Chadni")
#6.Non-repeating char
def first_non_repeating_char(name):
    
    cleaned_name = [char.lower() for char in name if char.isalpha()]
    
    
    char_count = {}
    for char in cleaned_name:
        char_count[char] = char_count.get(char, 0) + 1

    
    for char in cleaned_name:
        if char_count[char] == 1:
            print(f"First non-repeating character: '{char}'")
            return

    print("No non-repeating character found.")


first_non_repeating_char("Zakia Sultana Chadni")





