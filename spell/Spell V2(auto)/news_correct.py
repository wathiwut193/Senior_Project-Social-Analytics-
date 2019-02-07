import sys
from spellcheck import *
import time

read_text = open('news_1_ตัด.txt','r',encoding='utf-8')
text = read_text.read()
x = text.split("|")

start = time.time()
for i in x:
        if is_spelled_correctly(i):
                
        else:
            print(correction(i))

end = time.time()
print(end-start)