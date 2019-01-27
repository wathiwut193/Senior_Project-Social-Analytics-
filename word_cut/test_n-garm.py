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
corpus = 'corpus/คำศัพท์ที่ขึ้นต้นด้วยการ.txt'
read = codecs.open(corpus,'r','utf-8')
list_read = read.read()
list_read = list_read.split('\r\n')
read.close()
#print((list_read))
t0 = time.time()
ng = ngram.NGram(list_read)
b = ng.search('การฝึกงาร')
#print(b)
#print(type(b))
t1 = time.time()
print(t1-t0)
print(b[0])