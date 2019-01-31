import deepcut
read_data1 = 'เทศบาลเมืองแสนสุข ต.แสนสุข อ.เมืองชลบุรี จ.ชลบุรี'
read_data2 = 'เทศบาล เมืองแสนสุข ตำบล แสนสุข อำเภอ เมืองชลบุรี จังหวัด ชลบุรี'
read_data3 = 'ที่ถนนพระราม 2 ขาออก มุ่งหน้ามหาชัย ใกล้ซอย 83 แขวงแสมดำ เขตบางขุนเทียน กทม.'
read_data4 = 'ต.ลานข่อย อ.ป่าพะยอม จ.พัทลุง เสียชีวิตภายในบ้านหลังหนึ่ง ในหมู่บ้านภูเก็ตวิลล่า 5 ต.วิชิต อ.เมือง จ.ภูเก็ต'
read_data5 = 'เสียชีวิตคาที่บริเวณข้างคอกเลี้ยงวัวชนของ ส.จ.แอ๋วหรือนายสมชาย เกตุชาติ ส.อบจ.นครศรีธรรมราช เขต อ.เมือง ท้องที่หมู่ 4 ต.โพธิ์เสด็จ อ.เมือง จ.นครศรีธรรมราช เมื่อเย็นวันที่ 25 ม.ค.ที่ผ่านมา'

read_location1 = 'ถนนสุขุมวิท เทศบาลเมืองชลบุรี อำเภอเมือง จังหวัดชลบุรี'
read_location1_1 = 'ถนนสุขุมวิทเทศบาลเมืองชลบุรีอำเภอเมืองจังหวัดชลบุรี'

read_location2 = 'ถ.สุขุมวิท ทต.เมืองชลบุรี อ.เมือง จ.ชลบุรี'
read_location2_1 = 'ถ.สุขุมวิททต.เมืองชลบุรีอ.เมืองจ.ชลบุรี'

read_location3 = 'ถนนสุขุมวิท ตำบลอ่างศิลา อำเภอเมือง จังหวัดชลบุรี'
read_location3_1 = 'ถนนสุขุมวิทตำบลอ่างศิลาอำเภอเมืองจังหวัดชลบุรี'

read_location4 = 'ถ.สุขุมวิท ต.อ่างศิลา อ.เมือง จ.ชลบุรี'
read_location4_1 = 'ถ.สุขุมวิทต.อ่างศิลาอ.เมืองจ.ชลบุรี'

read_location5 = 'ถนนสุขุมวิท ตำบลท่าบุญมี กิ่งอำเภอเกาะจันทร์ จังหวัดชลบุรี'
read_location5_1 = 'ถนนสุขุมวิทตำบลท่าบุญมีกิ่งอำเภอเกาะจันทร์จังหวัดชลบุรี'

read_location6 = 'ถ.สุขุมวิท ต.ท่าบุญมี กิ่งอ.เกาะจันทร์ จ.ชลบุรี'
read_location6_1 = 'ถ.สุขุมวิทต.ท่าบุญมีกิ่งอ.เกาะจันทร์จ.ชลบุรี'

read_location7 = 'ถนนสุขุมวิท แขวงบางนา เขตบางนา กรุงเทพฯ'
read_location7_1 = 'ถนนสุขุมวิทแขวงบางนาเขตบางนากรุงเทพฯ'
read_location8 = 'ถ.สุขุมวิท แขวงบางนา เขตบางนา กรุงเทพมหานคร'
read_location8_1 = 'ถ.สุขุมวิทแขวงบางนาเขตบางนากรุงเทพมหานคร'
read_location9 = 'ถ.สุขุมวิท แขวงบางนา เขตบางนา กทม.'
read_location9_1 = 'ถ.สุขุมวิทแขวงบางนาเขตบางนากทม.'

corpus = 'corpus/compond_word.txt'
"""
word_cut1 = deepcut.tokenize(read_data1, custom_dict=corpus)
word_cut2 = deepcut.tokenize(read_data2, custom_dict=corpus)
word_cut3 = deepcut.tokenize(read_data3, custom_dict=corpus)
word_cut4 = deepcut.tokenize(read_data4, custom_dict=corpus)
word_cut5 = deepcut.tokenize(read_data5, custom_dict=corpus)
"""
word_cut1 = deepcut.tokenize(read_location1, custom_dict=corpus)
word_cut1_1 = deepcut.tokenize(read_location1_1, custom_dict=corpus)
word_cut2 = deepcut.tokenize(read_location2, custom_dict=corpus)
word_cut2_1 = deepcut.tokenize(read_location2_1, custom_dict=corpus)
word_cut3 = deepcut.tokenize(read_location3, custom_dict=corpus)
word_cut3_1 = deepcut.tokenize(read_location3_1, custom_dict=corpus)
word_cut4 = deepcut.tokenize(read_location4, custom_dict=corpus)
word_cut4_1 = deepcut.tokenize(read_location4_1, custom_dict=corpus)
word_cut5 = deepcut.tokenize(read_location5, custom_dict=corpus)
word_cut5_1 = deepcut.tokenize(read_location5_1, custom_dict=corpus)
word_cut6 = deepcut.tokenize(read_location6, custom_dict=corpus)
word_cut6_1 = deepcut.tokenize(read_location6_1, custom_dict=corpus)
word_cut7 = deepcut.tokenize(read_location7, custom_dict=corpus)
word_cut7_1 = deepcut.tokenize(read_location7_1, custom_dict=corpus)
word_cut8 = deepcut.tokenize(read_location8, custom_dict=corpus)
word_cut8_1 = deepcut.tokenize(read_location8_1, custom_dict=corpus)
word_cut9 = deepcut.tokenize(read_location9, custom_dict=corpus)
word_cut9_1 = deepcut.tokenize(read_location9_1, custom_dict=corpus)

print('================================================================================')
print(word_cut1)
print(word_cut1_1)
print('================================================================================')
print(word_cut2)
print(word_cut2_1)
print('================================================================================')
print(word_cut3)
print(word_cut3_1)
print('================================================================================')
print(word_cut4)
print(word_cut4_1)
print('================================================================================')
print(word_cut5)
print(word_cut5_1)
print('================================================================================')
print(word_cut6)
print(word_cut6_1)
print('================================================================================')
print(word_cut7)
print(word_cut7_1)
print('================================================================================')
print(word_cut8)
print(word_cut8_1)
print('================================================================================')
print(word_cut9)
print(word_cut9_1)
print('================================================================================')