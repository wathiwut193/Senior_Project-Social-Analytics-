"""
Create on 22 /1 /2019 11:57
@Coder Wathiwut Kongjan
"""
import deepcut
import codecs
import time
import re

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
    with codecs.open("news_mistake/input/news_15.txt",'r',encoding='utf-8') as readfile: #readfile
        data = readfile.read()
        cut = data.split('"')
        readfile.close()

    with codecs.open("news_mistake/output/news_15_ตัด.txt",'w+',encoding='utf-8') as write_split: #write_split
        write_split.write(''.join(cut))
        write_split.close()
    
    with codecs.open("news_mistake/output/news_15_ตัด.txt",'r+',encoding='utf-8') as readfile_split: #read_data
        read_data = readfile_split.read()
        word_cut = deepcut.tokenize(read_data, custom_dict='corpus/compond_word.txt')
        readfile_split.close()

    with codecs.open("news_mistake/output/news_15_ตัด.txt",'w+',encoding='utf-8') as writefile: #writefile
        writefile.read()
        writefile.write('|')
        writefile.write('|'.join(word_cut))
        writefile.write('|')
        writefile.close()

    print(word_cut)
    finnish_time = time.time()
    print(finnish_time-start_time)

def identify_tag():
    start_time =time.time()

    regex = r"(<[^<]*>[^<]*</[^<]*>)"
    read_str = ("คดีฆ่าพระ ยังอึมครึม วอนช่วยแก้ปัญหาดับไฟใต้!\n"
    "โดย ไทยรัฐฉบับพิมพ์<date>24 ม.ค. 2562</date> <time>04:30 น.</time>\n"
    "สมภารวัดดัง จ.นราธิวาส ระบุสถานการณ์ในพื้นที่ยังอึมครึม ออกจากวัดไปกิจนิมนต์แต่ละครั้งไม่รู้จะมีชีวิตกลับมาหรือไม่ ผวาหนักถึงขั้นลูกศิษย์ต้องพกปืนป้องกันตัว ค้านแนวคิด ผบ.ทบ.ที่จะให้ทหารบวชพระ ชี้หัวดื้อไม่ยอมปฏิบัติศาสนกิจ ขณะที่พระสงฆ์ใน อ.สุไหงปาดี ออกบิณฑบาตวันแรกหลังเกิดเหตุยิงถล่มวัดทำพระมรณภาพ 2 รูป ท่ามกลางการรักษาความปลอดภัยเข้มงวด ด้านชาวพุทธ 3 จังหวัดชายแดนใต้กว่า 600 คน ตั้งขบวนแห่เรียกร้องสันติ\n")
    matches = re.finditer(regex, read_str, re.MULTILINE)
    match_i = []
    for matchNum, match in enumerate(matches, start=1):
        #print ("Match {matchNum} was found at {start}-{end}: {match}".format(matchNum = matchNum, start = match.start(), end = match.end(), match = match.group()))
        #print ("Match:", matchNum)
        #print ("Start:", match.start() ,"End:", match.end())
        #print ("Result:", match.group())
        match_i.append(match.start()) #เก็บตำแหน่ง tag ตัวแรกที่เจอ
        match_i.append(match.end()) #เก็บตำแหน่ง tag ตัวสุดท้ายที่เจอ

    #print(match_i) #ดูข้อมูลเริ่มต้น สุดท้ายของ tag
    str_s = '' #สร้างตัวแปรมาเก็บ string ที่ไม่มี tag
    index_match=0 #สร้างตัวแปรเพื่อเช็ค index match_i
    str_tag = '' #สร้างตัวแปรมาเก็บ string ที่มี tag
    print(len(match_i)) #check index tag
    for i in range(len(read_str)):
        if index_match <= len(match_i):
            if index_match % 2 == 0: # if index_match % 2 = 0
                if index_match < len(match_i): # if index_match < length for match_i
                    if match_i[index_match] == i: #if match_i[index_match] = i
                        index_match = index_match  + 1 # ให้ทำการเพิ่มค่า index_match
                        str_tag += read_str[i] # ใส่ข้อมูลแรกของ tag ลงไปใน str_tag
                        str_s += ' =' #ใส่ช่องว่างให้ตัวสุดท้ายก่อนที่จะเจอ tag
                    else:   
                        str_s += read_str[i]  # else ให้เอาค่า str ตำแหน่ง i ไปใส่ใน str_s
                else:
                    str_s += read_str[i] # เก็บ str แถวสุดท้ายหลังจาก tag
            elif index_match % 2 != 0:
                if match_i[index_match] == i: #if match_i[index_match] = i
                    index_match = index_match  + 1 # ให้ทำการเพิ่มค่า index_match
                    str_tag += '\n' #ใส่ช่องว่างให้ตัวสุดท้ายให้หลัง tag
                else:
                    str_tag += read_str[i] # else ให้เอาค่า str ตำแหน่ง i ไปใส่ใน str_tag

    print(str_s)
    print('-------------------------------------')
    print(str_tag)
    print('-------------------------------------')
    tag_split = (str_tag.split('\n'))
    print(tag_split)
    word_cut = deepcut.tokenize(str_s, custom_dict='corpus/compond_word.txt')
    print(word_cut[20])
    
    ind = 0
    #word_cut = [w.replace('=',tag_split[ind]) for w in word_cut]
    
    for i in range(len(word_cut)):
        if word_cut[i] == '=':
            word_cut[i] = tag_split[ind]
            ind = ind + 1

    word = ''
    
    for i in range(len(word_cut)):
        if word_cut[i] != '=':
            word = ('|'.join(word_cut))
    
    print(word)
    finnish_time = time.time()
    print(finnish_time-start_time)


identify_tag()

#newsreader_wordcut()