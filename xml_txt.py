# 项目名称：xml_txt_mutual_conversion
# 程序内容：xml转txt
# 作   者：MBJC
# 开发时间：2022/8/1 11:29

import xml.etree.ElementTree as ET
import os
from os import getcwd
import glob

# 1.
# 自己创建文件夹,例如：label_mal label_txt  也可以修改别的
image_set = 'xml'  # 需要转换的文件夹名称（文件夹内放xml标签文件）
imageset2 = 'txt'  # 保存txt的文件夹
# 2.
# 换成你的类别 当前的顺序，就txt 0,1,2,3 四个类别
classes = ['car', 'horse', 'chair', 'bicycle']  # 标注时的标签 注意顺序一定不要错。

# 3.
# # 转换文件夹的绝对路径
# data_dir = 'D:/detectAuto_/data'
# 或者 读取当前路径
data_dir = getcwd()  # 当前路径


'''
xml中框的左上角坐标和右下角坐标(x1,y1,x2,y2)
》》txt中的中心点坐标和宽和高(x,y,w,h)，并且归一化
'''


def convert(size, box):
    dw = 1. / size[0]
    dh = 1. / size[1]
    x = (box[0] + box[1]) / 2.0
    y = (box[2] + box[3]) / 2.0
    w = box[1] - box[0]
    h = box[3] - box[2]
    x = x * dw
    w = w * dw
    y = y * dh
    h = h * dh
    return (x, y, w, h)


def convert_annotation(data_dir, imageset1, imageset2, image_id):
    in_file = open(data_dir + '/%s/%s.xml' % (imageset1, image_id))  # 读取xml
    out_file = open(data_dir + '/%s/%s.txt' % (imageset2, image_id), 'w')  # 保存txt

    tree = ET.parse(in_file)
    root = tree.getroot()
    size = root.find('size')
    w = int(size.find('width').text)
    h = int(size.find('height').text)
    for obj in root.iter('object'):
        difficult = obj.find('difficult').text
        cls = obj.find('name').text
        if cls not in classes or int(difficult) == 1:
            continue
        cls_id = classes.index(cls)  # 获取类别索引
        xmlbox = obj.find('bndbox')
        b = (float(xmlbox.find('xmin').text), float(xmlbox.find('xmax').text), float(xmlbox.find('ymin').text),
             float(xmlbox.find('ymax').text))
        bb = convert((w, h), b)
        out_file.write(str(cls_id) + " " + " ".join([str('%.6f' % a) for a in bb]) + '\n')


image_ids = []
for x in glob.glob(data_dir + '/%s' % image_set + '/*.xml'):
    image_ids.append(os.path.basename(x)[:-4])
print('\n%s数量:' % image_set, len(image_ids))  # 确认数量
i = 0
for image_id in image_ids:
    i = i + 1
    convert_annotation(data_dir, image_set, imageset2, image_id)
    print("%s 数据:%s/%s文件完成！" % (image_set, i, len(image_ids)))

print("Done!!!")



