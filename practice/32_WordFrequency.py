'''
32_WordFrequency.py
Words Frequency in a Sentence
Count Word Frequency

Design a Python function named count_word_frequency to count the frequency of words in a sentence and store the counts in a dictionary.

Parameters:

sentence (str): The input sentence where you need to count the frequency of each word.

Returns:

A dictionary where the keys are words from the sentence and the values are their corresponding frequencies.

Example:

Input: "hello world hello"
Output: {'hello': 2, 'world': 1}

Input: "the quick brown fox jumps over the lazy dog"
Output: {'the': 2, 'quick': 1, 'brown': 1, 'fox': 1, 'jumps': 1, 'over': 1, 'lazy': 1, 'dog': 1}
'''

## SOLUTION

def count_word_frequency(sentence):
    word_count = {}
    words = sentence.split()
    for word in words:
        if word in word_count:
            word_count[word] += 1
        else:
            word_count[word] = 1
    return word_count

print(count_word_frequency("hello world hello"))
