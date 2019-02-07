import sys
from spellcheck import *
import time


read_text = open('print.txt','r',encoding='utf-8')
text = read_text.read()
x = text.split("|")



t0 = time.time()
print(str(x))
for i in x:
        if is_spelled_correctly(i):
                """print(spell(i))"""
                
        else :
                print("Wrong spell: " + i)
                """
                x = [y.replace(i,(correction(i))) for y in x]
                print(x)
                read_text.close()
                """
                """
                print("Recommend word: " + str(spell(i)))
                """
                """
                
                x = [y.replace(i,(correction(i))) for y in x]
                new_text = open('new3.txt','w',encoding='utf-8')
                text2 = new_text.write('|'.join(x))
                new_text.close()
                

                """
                edit = input("Did you want to edit ?[Y/N]: ")
                if edit=='Y' or edit=='y':        
                        j = input("Insert a new word... ")
                        x = [y.replace(i,j) for y in x]
                        print(str(x))
                 
                        new_text = open('newprint.txt','w',encoding='utf-8')
                        text2 = new_text.write('|'.join(x))
                        new_text.close()

                
             
"""
values = sys.argv[1:]
        
for value in values:
    if not is_spelled_correctly(value):
        print("Wrong spell: " + value)

        print("Recommend word: " + str(spell(value)))
"""       
t1 = time.time()
print(t1-t0)