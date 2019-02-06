# Auto Correction

Auto correction is a one part function of Senior Project-Social-Analytics-.
It's correcting the word that have a wrong spelling to nearest probability correct word.
This demo was developed based on Pythainlp.

## Installation
```bash
$ pip install pythainlp
```
Pythainlp library from https://github.com/PyThaiNLP/pythainlp in spell correction function.

## Usage

Using Pythainlp for correcting word
```python
from pythainlp.spell.pn import *

spell('word') # Insert a word for correcting and it returns a list of spell candidate words.
correction('word') # Insert a word for correcting and it returns a nearest probability one correction word.
```
Using our demo 
```python
from spellcheck import *

correction('word') # Insert a word for correcting and it returns a nearest probability one correction word.
```
