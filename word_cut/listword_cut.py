"""
Create on 22 /1 /2019 11:57

@Coder Wathiwut Kongjan
"""
import deepcut
import time

def newsreader_wordcut():
    start_time =time.time()

    """
    How :
        Read text for file .txt and Cut word 
        File manual input 
        Output are write new file 

    Reference :
        Dictionary custom by add compond word from Wikipedia
    """
    with open("news/input/2.txt",'r',encoding='utf-8') as readfile: #readfile
        data = readfile.read()
        word_cut = deepcut.tokenize(data, custom_dict='compond_word.txt')


    with open("news/output/2_ตัด.txt",'w+',encoding='utf-8') as writefile: #writefile
        writefile.read()
        writefile.write('|'.join(word_cut))

    print(word_cut)
    finnish_time = time.time()
    print(finnish_time-start_time)

newsreader_wordcut()