import deepcut
read_data_time1 = '09:22 น.'
read_data_time2 = '16:47 น.'
read_data_time3 = '09.22 น.'
read_data_time4 = '16.47 น.'
read_data_time5 = '09:22 นาฬิกา'
read_data_time6 = '16:47 นาฬิกา'
read_data_time7 = '09.22 นาฬิกา'
read_data_time8 = '16.47 นาฬิกา'

corpus = 'corpus/compond_word.txt'

word_cut1 = deepcut.tokenize(read_data_time1, custom_dict=corpus)
word_cut2 = deepcut.tokenize(read_data_time2, custom_dict=corpus)
word_cut3 = deepcut.tokenize(read_data_time3, custom_dict=corpus)
word_cut4 = deepcut.tokenize(read_data_time4, custom_dict=corpus)
word_cut5 = deepcut.tokenize(read_data_time5, custom_dict=corpus)
word_cut6 = deepcut.tokenize(read_data_time6, custom_dict=corpus)
word_cut7 = deepcut.tokenize(read_data_time7, custom_dict=corpus)
word_cut8 = deepcut.tokenize(read_data_time8, custom_dict=corpus)

print(word_cut1)
print(word_cut2)
print(word_cut3)
print(word_cut4)
print(word_cut5)
print(word_cut6)
print(word_cut7)
print(word_cut8)