"""
Create on 22 /1 /2019 11:57

@Coder Wathiwut Kongjan
"""
import deepcut
import codecs
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
    with codecs.open("news/input/2.txt",'r',encoding='utf-8') as readfile: #readfile
        data = readfile.read()
        cut = data.split('"')
        readfile.close()

    with codecs.open("news/output/2_ตัด.txt",'w+',encoding='utf-8') as write_split: #write_split
        write_split.write(''.join(cut))
        write_split.close()
    
    with codecs.open("news/output/2_ตัด.txt",'r+',encoding='utf-8') as readfile_split: #read_data
        read_data = readfile_split.read()
        word_cut = deepcut.tokenize(read_data, custom_dict='compond_word.txt')
        readfile_split.close()

    with codecs.open("news/output/2_ตัด.txt",'w+',encoding='utf-8') as writefile: #writefile
        writefile.read()
        writefile.write('|'.join(word_cut))
        writefile.close()

    print(word_cut) #da
    finnish_time = time.time()
    print(finnish_time-start_time)

newsreader_wordcut()