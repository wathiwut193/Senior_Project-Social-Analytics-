import deepcut
read_data = 'เทศบาลเมืองแสนสุข ต.แสนสุข อ.เมืองชลบุรี จ.ชลบุรี'
read_data1 = 'เทศบาล เมืองแสนสุข ตำบล แสนสุข อำเภอ เมืองชลบุรี จังหวัด ชลบุรี'
read_data2 = 'ที่ถนนพระราม 2 ขาออก มุ่งหน้ามหาชัย ใกล้ซอย 83 แขวงแสมดำ เขตบางขุนเทียน กทม.'
read_data3 = 'ต.ลานข่อย อ.ป่าพะยอม จ.พัทลุง เสียชีวิตภายในบ้านหลังหนึ่ง ในหมู่บ้านภูเก็ตวิลล่า 5 ต.วิชิต อ.เมือง จ.ภูเก็ต'
read_data4 = 'เสียชีวิตคาที่บริเวณข้างคอกเลี้ยงวัวชนของ ส.จ.แอ๋วหรือนายสมชาย เกตุชาติ ส.อบจ.นครศรีธรรมราช เขต อ.เมือง ท้องที่หมู่ 4 ต.โพธิ์เสด็จ อ.เมือง จ.นครศรีธรรมราช เมื่อเย็นวันที่ 25 ม.ค.ที่ผ่านมา'

word_cut = deepcut.tokenize(read_data4, custom_dict='compond_word.txt')

#print(word_cut)

import ngram
a = ngram.NGram.compare('การ','การทำงาย',N=1)
#print(a)

G = ngram.NGram(['joe','joseph','jon','john','sally'])
x = G.search('jon')
print(x)
G.search('jon', threshold=0.3)
G.find('jose')


index = ngram.NGram(N=5)
z = list(index.ngrams(index.pad("การ")))
#print(z)

import codecs
import time
read = codecs.open('คำศัพท์ที่ขึ้นต้นด้วยการ.txt','r','utf-8')
list_read = read.read()
list_read = list_read.split('\r\n')
read.close()
#print((list_read))
t0 = time.time()
ng = ngram.NGram(list_read)
b = ng.search('การฝึกงาร')
print(b)
#print(type(b))
t1 = time.time()
print(t1-t0)
print(b[0])