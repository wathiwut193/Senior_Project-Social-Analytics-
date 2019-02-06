import sys
from spellcheck import *


values = sys.argv[1:]
        

for value in values:
    if not is_spelled_correctly(value):
        print("Wrong spell: " + value)
        print("Candidate words: " + str(spell(value)))
        print("Auto correct word: " + (correction(value)))
        
