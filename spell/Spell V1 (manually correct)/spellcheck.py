import re
from collections import Counter
from pythainlp.corpus.thaiword import get_data

dictionary = set()

def read_dictionary_file():
    global dictionary

    if dictionary:
        return


    with open("thaiword.txt","r",encoding="utf8") as f:
        contents = f.read()

    dictionary = set(
        word.lower()
        for word in contents.splitlines()
    )


def is_spelled_correctly(word):

    word = word.lower()
    read_dictionary_file()
    return word in dictionary

WORDS = Counter(get_data())

letters = ['ก', 'ข', 'ฃ', 'ค', 'ฅ', 'ฆ', 'ง', 'จ', 'ฉ', 'ช', 'ซ', 'ฌ', 'ญ', 'ฎ', 'ฏ', 'ฐ', 'ฑ', 'ฒ', 'ณ', 'ด', 'ต', 'ถ', 'ท', 'ธ', 'น', 'บ', 'ป', 'ผ', 'ฝ', 'พ', 'ฟ', 'ภ', 'ม', 'ย', 'ร', 'ฤ', 'ล', 'ฦ', 'ว', 'ศ', 'ษ', 'ส', 'ห', 'ฬ', 'อ', 'ฮ', 'ฯ', 'ะ', 'ั', 'า', 'ำ', 'ิ', 'ี', 'ึ', 'ื', 'ุ', 'ู', 'ฺ', '\u0e3b', '\u0e3c', '\u0e3d', '\u0e3e', '฿', 'เ', 'แ', 'โ', 'ใ', 'ไ', 'ๅ', 'ๆ', '็', '่', '้', '๊', '๋', '์']

def _no_filter(word):
    return True


def _is_thai_and_not_num(word):
    for ch in word:
        if ch != "." and not is_thaichar(ch):
            return False
        if ch in "๐๑๒๓๔๕๖๗๘๙0123456789":
            return False
    return True


def _keep(word_freq, min_freq, min_len, max_len, dict_filter):
    """
    Keep only Thai words with at least min_freq frequency
    and has length between min_len and max_len characters
    """
    if not word_freq or word_freq[1] < min_freq:
        return False

    word = word_freq[0]
    if not word or len(word) < min_len or len(word) > max_len or word[0] == ".":
        return False

    return dict_filter(word)

def P(word, N=sum(WORDS.values())):
    'Probability of `word`.'
    return WORDS[word] / N

def correction(word):
    'แสดงคำที่เป็นไปได้มากที่สุด'
    return max(spell(word), key=P)
def known(words):
    return list(w for w in words if w in WORDS)

def edits1(word):
    splits     = [(word[:i], word[i:])    for i in range(len(word) + 1)]
    deletes    = [L + R[1:]               for L, R in splits if R]
    transposes = [L + R[1] + R[0] + R[2:] for L, R in splits if len(R)>1]
    replaces   = [L + c + R[1:]        for L, R in splits if R for c in letters]
    inserts    = [L + c + R         for L, R in splits for c in letters]
    return set(deletes + transposes + replaces + inserts)
def edits2(word):
    return (e2 for e1 in edits1(word) for e2 in edits1(e1))
    
"""
def keyboardlayout(word) :   
    if letters=='ๅ'
"""
"""
def autocorrect(word):
    x = [(word[:i], word[i:])    for i in range(len(word) + 1)]
    a = [L + c + R              for L,R in x for c in letters]
    b = [L + c + R[1:]           for L,R in x if L for c in letters]
    kl = [L + c + R[1:]           for L,R in x if L for c in letters
        
        ]
    return  known(kl)
"""
num = ['๐','๑','๒','๓','๔','๕','๖','๗','๘','๙','0','1','2','3','4','5','6','7','8','9']

def condition(word):
    if word=='มากก' or word=='มากกก' or word=='มากกกก' or word=='มากกกกก' or word=='มากกกกกก':
            return ['มากๆ']
    elif word==' ' :
            return [' ']
    elif word in num:
            return str(word)
            


def spell(word):
    if word=='':
        return ''
    else:

        return (known([word]) or (condition(word)) or known(edits1(word)) or known(edits2(word)) or [word])


        

