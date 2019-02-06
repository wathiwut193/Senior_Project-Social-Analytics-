# -*- coding: utf-8 -*-
from __future__ import absolute_import,unicode_literals
import os
import codecs
import pythainlp
templates_dir = os.path.join(os.path.dirname(pythainlp.__file__), 'corpus')
"""
template_file1 = os.path.join(templates_dir, 'country(big).txt')
template_file2 = os.path.join(templates_dir, 'province.txt')
template_file3 = os.path.join(templates_dir, 'Prefecture.txt')
template_file4 = os.path.join(templates_dir, 'District.txt')
template_file5 = os.path.join(templates_dir, 'Road.txt')
"""
#places.txt คือไฟล์dict รวม 5 ไฟล์ ได้แก่ ประเทศ จังหวัด อำเภอ ตำบล และถนน 
template_file1 = os.path.join(templates_dir, 'places.txt') 

def get_data():
    """
    with codecs.open(template_file1, 'r',encoding='utf8') as cou,codecs.open(template_file2, 'r',encoding='utf8') as pro,codecs.open(template_file3, 'r',encoding='utf8') as pre,codecs.open(template_file4, 'r',encoding='utf8') as dis,codecs.open(template_file5, 'r',encoding='utf8') as roa:
        for i in cou,pro,pre,dis,roa:
            i = cou.read().splitlines() + pro.read().splitlines() + pre.read().splitlines()+ dis.read().splitlines() + roa.read().splitlines()
            return i 
    """              
    with codecs.open(template_file1, 'r+',encoding='utf8') as p:
        i = p.read().splitlines()
        return i