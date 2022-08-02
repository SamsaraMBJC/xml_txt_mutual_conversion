# 项目名称：DI_QueXianShiJueJianCe
# 程序内容：修改xml标签名
# 作   者：MBJC
# 开发时间：2022/7/10 8:30

"""
批量修改xml文件中的缺陷类别名称
当有多个物体时，多个物体的名称均能被修改
"""

from lxml.etree import Element, SubElement, tostring, ElementTree
from xml.dom import minidom
import xml.etree.ElementTree as ET
import os
# 修改自己的路径
template_file = r'E:\CSDN\xml_txt_mutual_conversion\xml'  #这里是存放xml文件的文件夹
xmllist = os.listdir(template_file)
for xml in xmllist:
    #print(xml)
    tree = ET.parse(os.path.join(template_file,xml))
    root = tree.getroot() # 获取根节点
    for child in root:
        print(child.tag,child.attrib)
        if child.tag == 'object':
            name=child.find('name').text
            # print(name)
            if name == '1':
                child.find('name').text = 'car'
                tree=ET.ElementTree(root)
            elif name == '2':
                child.find('name').text = 'horse'
                tree = ET.ElementTree(root)
            elif name == '3':
                child.find('name').text = 'chair'
                tree = ET.ElementTree(root)
            elif name == '4':
                child.find('name').text = 'bicycle'
                tree = ET.ElementTree(root)
    tree.write(os.path.join(template_file,xml))
