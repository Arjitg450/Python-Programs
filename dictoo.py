import nltk
import numpy as np
import random
import string # to process standard python strings
while True: 
    inp=input("Enter the word: ")
    from nltk.corpus import wordnet
    

    print("MEANING: ",wordnet.synset('{}.n.01'.format(inp)).definition())
    print("EXAMPLE: ",wordnet.synset('{}.n.01'.format(inp)).examples())
    print("MEANING: ",wordnet.synset('{}.n.02'.format(inp)).definition())
    print("EXAMPLE: ",wordnet.synset('{}.n.02'.format(inp)).examples())


