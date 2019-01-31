import ngram
a = ngram.NGram.compare('การ','การทำงาย',N=1)
#print(a)

#G = ngram.NGram(['joe','joseph','jon','john','sally'])
#x = G.search('jon')
#print(x)
#G.search('jon', threshold=0.3)
#G.find('jose')

index = ngram.NGram(N=5)
z = list(index.ngrams(index.pad("การ")))
#print(z)

import codecs
import time
corpus = 'corpus/new-thaidict.txt'
read = codecs.open(corpus,'r','utf-8')
list_read = read.read()
list_read = list_read.split('\n')
read.close()
#print((list_read))

read_news = codecs.open('news/output/จับ2หนุ่ม โชว์ปืนขู่เด็กปั๊ม แถมดูดกัญชา โดนไป 4 ข้อหา_ตัด.txt','r+','utf-8')
reads = read_news.read()
read_news.close()
"""
st = '|จับ|2|หนุ่ม| |โชว์|ปืน|ขู่|เด็ก|ปั๊ม| |แถม|ดูด|กัญชา| |โดน|ไป| |5| |ข้อ|หา|'
text_split = st.split('|')

print(type(text_split[0]))
print(text_split)
t0 = time.time()
ng = ngram.NGram(list_read)
#b = ng.search('ได่')

t = []
for i in range(len(text_split)):
    if text_split[i] != ' ':
        if text_split[i] != '':
            if text_split[i].isdigit() == True: #check string is int ex. '5'
                #print(sp[i])
                t.append(text_split[i])
            else:
                #print(sp[i])
                t.append(ng.search(text_split[i]))
                

for i in range(len(t)):
    if t[i]:
        print(t[i][0])

t1 = time.time()
print(t1-t0)
"""
ng = ngram.NGram(list_read)
st = '|จับ|2|หนุ่ม| |โชว์|ปืน|ขู่|เด็ก|ปั๊ม| |แถม|ดูด|กัญชา| |โดน|ไป| |5| |ข้อ|หา|'

st_r = ['จับ','2','หนุ่ม','โชว์','ปืน','ขู่','เด็ก','ปั๊ม','แถม','ดูด','กัญชา','โดน','ไป','5','ข้อ','หา']
res = []
inde = []
li = []
#print(len(st_r))
for i in range(len(st_r)):
    if i != len(st_r)-1:
        if (st_r[i].isdigit() != True)and(st_r[i+1].isdigit() != True):
            li.append(st_r[i]+st_r[i+1])
            if ng.search(st_r[i]+st_r[i+1], threshold=1.0):
                print(st_r[i]+st_r[i+1])
                res.append(st_r[i]+st_r[i+1])
                inde.append(i)
                inde.append(i+1)
            #print(st_r[i]+st_r[i+1])
        elif (st_r[i].isdigit() == True):
            #print(st_r[i])
            li.append(st_r[i])
        else:
            li.append(st_r[i])
    else:
        #print(st_r[i])
        li.append(st_r[i])

print(res)
print(inde)
c = []
"""
for i in range(len(li)):
    if ng.search(li[i], threshold=1.0):
        print('true')
        c.append(ng.search(li[i], threshold=1.0))
    else:
        print('false')
""" 

#print(c[0][0])
#print(c[1][0])
#print(c[2][0])