# 项目名称：DI_QueXianShiJueJianCe
# 程序内容：修改txt标签名称
# 作   者：MBJC
# 开发时间：2022/7/26 11:10

import os
import re
# 路径
path = './txt/'
# 文件列表
files = []
for file in os.listdir(path):
    if file.endswith(".txt"):
        files.append(path+file)
# 逐文件读取-修改-重写
for file in files:
    with open(file, 'r') as f:
        new_data = re.sub('^0', 'car', f.read(), flags=re.MULTILINE)  # 将列中的0替换为car
    with open(file, 'w') as f:
        f.write(new_data)
    with open(file, 'r') as f:
        new_data = re.sub('^1', 'horse', f.read(), flags=re.MULTILINE)  # 将列中的1替换为horse
    with open(file, 'w') as f:
        f.write(new_data)
    with open(file, 'r') as f:
        new_data = re.sub('^2', 'chair', f.read(), flags=re.MULTILINE)  # 将列中的2替换为chair
    with open(file, 'w') as f:
        f.write(new_data)
    with open(file, 'r') as f:
        new_data = re.sub('^3', 'bicycle', f.read(), flags=re.MULTILINE)  # 将列中的3替换为bicycle
    with open(file, 'w') as f:
        f.write(new_data)


