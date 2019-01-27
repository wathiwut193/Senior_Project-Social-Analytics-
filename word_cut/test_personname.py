import deepcut

news_head = 'จับ2หนุ่ม โชว์ปืนขู่เด็กปั๊ม แถมดูดกัญชา โดนไป 4 ข้อหา'
news_by = 'โดย ไทยรัฐออนไลน์'
news_time = '27 ม.ค. 2562 14:38 น.'

read_data_personname1 = 'พล.ต.ต.สำราญ นวลมา'
read_data_personname2 = 'พ.ต.อ.สมบูรณ์ เทียนขาว'
read_data_personname3 = 'พ.ต.ท.อานันท์จักร์ กนกนพวัชร์'
read_data_personname4 = 'นายแบ้ง ทองแท้'
read_data_personname5 = 'นายกฤษฎา โป๊ะแก้ว'

read_data_personname6 = 'พ.ต.อ.สำราญ'
read_data_personname7 = 'พ.ต.อ.สมบูรณ์'
read_data_personname8 = 'พ.ต.ท.อานันท์จักร์'
read_data_personname9 = 'นายแบ้ง'
read_data_personname10 = 'นายกฤษฎา'

read_data_personname11 = 'สำราญ นวลมา'
read_data_personname12 = 'สมบูรณ์ เทียนขาว'
read_data_personname13 = 'อานันท์จักร์ กนกนพวัชร์'
read_data_personname14 = 'แบ้ง ทองแท้'
read_data_personname15 = 'กฤษฎา โป๊ะแก้ว'

read_data_personname16 = 'สำราญ'
read_data_personname17 = 'สมบูรณ์'
read_data_personname18 = 'อานันท์จักร์'
read_data_personname19 = 'แบ้ง'
read_data_personname20 = 'กฤษฎา'

read_data_personname21 = 'นวลมา'
read_data_personname22 = 'เทียนขาว'
read_data_personname23 = 'กนกนพวัชร์'
read_data_personname24 = 'ทองแท้'
read_data_personname25 = 'โป๊ะแก้ว'

corpus = 'corpus/compond_word.txt'

word_cut1 = deepcut.tokenize(read_data_personname1, custom_dict=corpus)
word_cut2 = deepcut.tokenize(read_data_personname2, custom_dict=corpus)
word_cut3 = deepcut.tokenize(read_data_personname3, custom_dict=corpus)
word_cut4 = deepcut.tokenize(read_data_personname4, custom_dict=corpus)
word_cut5 = deepcut.tokenize(read_data_personname5, custom_dict=corpus)
word_cut6 = deepcut.tokenize(read_data_personname6, custom_dict=corpus)
word_cut7 = deepcut.tokenize(read_data_personname7, custom_dict=corpus)
word_cut8 = deepcut.tokenize(read_data_personname8, custom_dict=corpus)
word_cut9 = deepcut.tokenize(read_data_personname9, custom_dict=corpus)
word_cut10 = deepcut.tokenize(read_data_personname10, custom_dict=corpus)
word_cut11 = deepcut.tokenize(read_data_personname11, custom_dict=corpus)
word_cut12 = deepcut.tokenize(read_data_personname12, custom_dict=corpus)
word_cut13 = deepcut.tokenize(read_data_personname13, custom_dict=corpus)
word_cut14 = deepcut.tokenize(read_data_personname14, custom_dict=corpus)
word_cut15 = deepcut.tokenize(read_data_personname15, custom_dict=corpus)
word_cut16 = deepcut.tokenize(read_data_personname16, custom_dict=corpus)
word_cut17 = deepcut.tokenize(read_data_personname17, custom_dict=corpus)
word_cut18 = deepcut.tokenize(read_data_personname18, custom_dict=corpus)
word_cut19 = deepcut.tokenize(read_data_personname19, custom_dict=corpus)
word_cut20 = deepcut.tokenize(read_data_personname20, custom_dict=corpus)
word_cut21 = deepcut.tokenize(read_data_personname21, custom_dict=corpus)
word_cut22 = deepcut.tokenize(read_data_personname22, custom_dict=corpus)
word_cut23 = deepcut.tokenize(read_data_personname23, custom_dict=corpus)
word_cut24 = deepcut.tokenize(read_data_personname24, custom_dict=corpus)
word_cut25 = deepcut.tokenize(read_data_personname25, custom_dict=corpus)

print('===========================')
print(word_cut1)
print(word_cut2)
print(word_cut3)
print(word_cut4)
print(word_cut5)
print('===========================')
print(word_cut6)
print(word_cut7)
print(word_cut8)
print(word_cut9)
print(word_cut10)
print('===========================')
print(word_cut11)
print(word_cut12)
print(word_cut13)
print(word_cut14)
print(word_cut15)
print('===========================')
print(word_cut16)
print(word_cut17)
print(word_cut18)
print(word_cut19)
print(word_cut20)
print('===========================')
print(word_cut21)
print(word_cut22)
print(word_cut23)
print(word_cut24)
print(word_cut25)
print('===========================')