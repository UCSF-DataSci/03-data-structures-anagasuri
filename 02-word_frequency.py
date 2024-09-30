#!/usr/bin/env python3
"""
Word Frequency Counter

This script reads a text file and counts the frequency of each word, ignoring case.

Usage: python word_frequency.py <input_file>


Your task:
- Complete the word_frequency() function to count word frequencies sorted alphabetically
- Test your script on 'alice_in_wonderland.txt'

Hints:
- Use a dictionary to store word frequencies
- Consider using the lower() method to ignore case
- The split() method can be useful for splitting text into words
"""

import sys

def word_frequency(text):
    frequencies = {} # Dictionary to store word frequencies
    
    # Your code here
    clean_text = []  # initialize empty array for cleaned version of text 

    # replace all punctuation and new lines with a space 
    text = text.replace("\n", " ")
    text = text.replace(",", " ")
    text = text.replace(".", " ")
    text = text.replace("?", " ")
    text = text.replace(";", " ")
    text = text.replace('"', " ")
    text = text.replace("'"," ")
    text = text.replace("-", " ")
    text = text.replace("_", " ")
    text = text.replace("!", " ")
    text = text.replace("(", " ")
    text = text.replace(")", " ")
    text = text.replace(":", " ")
    text = text.replace("[", " ")
    text = text.replace("]", " ")
    text = text.replace("*","") # take out all *, not words so don't count frequency 

    for word in text.split(" "): # split the string at each spaces 
        word = word.lower() # converts all words to lowercase 
        clean_text.append(word) # every cleaned word is appended to the empty clean_text array 

    for word in clean_text:  # iterate through ever word in this verison of the cleaned text 
        if word == "": # if the word is empty, then skip this iteration of the loop and move onto the next word 
            continue;       
        if word not in frequencies: # if the word does not exist as a key in frequency
            frequencies[word] = 1 # create a new key and set it to count 1 
        if word in frequencies: # if the word already exists as a key in frequency 
            frequencies[word] += 1 # increment the key's value by 1 

    sorted_frequencies = {} # create empty dict to sort keys 
    for key in sorted(frequencies): # for every key in the alphabetically sorted frequencies dict
        sorted_frequencies[key] = frequencies[key] # pull the value of the key and assign it to the sorted version of the same key in sorted_frequencies dict 

    frequencies = sorted_frequencies # reassign the newly sorted dict to the old dict name 

    return frequencies #return sorted dictionary 

# Scaffold for opening a file and running word_frequency() on the contents
if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python word_frequency.py <input_file>")
        sys.exit(1)
    
    filename = sys.argv[1]
    try:
        with open(filename, 'r') as file:
            text = file.read() # Read the entire file into a string
        
        frequencies = word_frequency(text)
        
        # Print results
        for word, count in frequencies.items():
            print(f"{word}: {count}")
    
    except FileNotFoundError:
        print(f"Error: File '{filename}' not found.")
        sys.exit(1)
    
    print(f"Word frequencies for '{filename}':")
    print(frequencies)