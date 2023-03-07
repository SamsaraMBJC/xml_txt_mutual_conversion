# xml_txt_mutual_conversion
VOC Yolo tag modification conversion script

Github：

链接: [https://github.com/Samsara0Null/xml_txt_mutual_conversion](https://github.com/Samsara0Null/xml_txt_mutual_conversion)

CSDN主页：

链接: [https://blog.csdn.net/noneNull0?type=blog](https://blog.csdn.net/noneNull0?type=blog)

Bilibili视频演示讲解：

链接: [https://www.bilibili.com/video/BV1ie4y1D77dvd_source=a6067b731745325c01a4edfa46bf5a04](https://www.bilibili.com/video/BV1ie4y1D77d?vd_source=a6067b731745325c01a4edfa46bf5a04)

umm，评论区有提出在使用txt_xml.py时，标签为字符类型，会报类似ValueError: could not convert string 'A' to float64 at row 0, column 1.
雀氏有道理，简单修改了一下，作为补充，用法同之前，修改路径，应该可以直接用，有相关需求可以尝试一下

链接: [https://wwin.lanzoue.com/i12Yt0pj83fg](https://wwin.lanzoue.com/i12Yt0pj83fg)

## 这是一些帮助转换txt和xml格式标签文件格式和修改标签名称的脚本（适用于VOC-yolo项目格式的标签）
### 可能需要安装一些依赖，配置好环境（跟着MoudleNotFound报错走就好了）
### 我的环境：
- VSCode+Anaconda
- python==3.6.13
- pillow==8.3.1
- opencv-python==4.6.0.66
- numpy==1.19.5
- lxml==3.8.0 
### 演示样本：
![在这里插入图片描述](https://img-blog.csdnimg.cn/c9756516fd234ff6bc64e5ee54571bfe.png)
![在这里插入图片描述](https://img-blog.csdnimg.cn/36050202a84f4cb0bddc7762ec7227ae.png)
## txt_change_label.py
- 代码作用：修改txt标签名称
- 1、修改存放txt标签文件的文件夹路径
    这里用了相对脚本的路径
 
![在这里插入图片描述](https://img-blog.csdnimg.cn/ec53d0c1f9cf475a8273c90c1b08130f.png)

- 2、依葫芦画瓢修改想要的修改前和修改后标签名称

![在这里插入图片描述](https://img-blog.csdnimg.cn/38fba089a1e842bfb461a1825ca3fa54.png)

- 3、运行 txt_change_label.py

![在这里插入图片描述](https://img-blog.csdnimg.cn/99bcdc461fcf46a1be7f1692ccfb97f5.png)

- 4、结果展示

运行前：
 
![在这里插入图片描述](https://img-blog.csdnimg.cn/e12b739bcf5e47119c916fe3a09c43ef.png)

运行后：
 
![在这里插入图片描述](https://img-blog.csdnimg.cn/63d35cb7fc2d46fda2c574cc2b6242c3.png)

## txt_xml.py
- 代码作用：txt标签格式和对应jpg图片转换xml标签格式
- 1、txt和对应jpg放在同一文件夹内

![在这里插入图片描述](https://img-blog.csdnimg.cn/a54a194eeb7044ca98b2e8de631dc3bb.png)
- 2、修改目标文件夹路径

![在这里插入图片描述](https://img-blog.csdnimg.cn/d9336cdd1d1d45df82978d2e2c239d72.png)
- 3、运行txt_xml.py

![在这里插入图片描述](https://img-blog.csdnimg.cn/8db596b3289a4ce9a6f09d80bd18073d.png)

- 4、结果展示

运行前：

![在这里插入图片描述](https://img-blog.csdnimg.cn/3a897ea19e5343a780202a49b3f0d2e9.png)

运行后：

![在这里插入图片描述](https://img-blog.csdnimg.cn/8c38b35d6c704beebbde1a8558129c40.png)

可在labelimg中打开（注意txt中的标签0会变成xml中的标签1）

![在这里插入图片描述](https://img-blog.csdnimg.cn/89c9092899d04714b20690a4830b3f60.png)

![在这里插入图片描述](https://img-blog.csdnimg.cn/95742c0c260649d68813be6285ce053c.png)

在文件夹中搜索xml即可得到文件

![在这里插入图片描述](https://img-blog.csdnimg.cn/de600f7dce574fb190528fdaf231f9d3.png)
## xml_change_label.py
- 代码作用：修改xml标签名称
- 1、修改存放xml标签文件的文件夹路径

![在这里插入图片描述](https://img-blog.csdnimg.cn/f9105660de0249d0a8dae68be72b26d2.png)
- 2、修改自己想要修改的标签，例：1->car，标签数不同删减或增加elif语句即可

![在这里插入图片描述](https://img-blog.csdnimg.cn/b3a06933ee44423f835452e2f5b3c172.png)
- 3、运行xml_change_label.py

![在这里插入图片描述](https://img-blog.csdnimg.cn/f5bee56047ea48a5b284e74db8a8c4dd.png)

- 4、结果展示

运行前：
    
![在这里插入图片描述](https://img-blog.csdnimg.cn/2e4e1af96b6841ff8ec46e93593e4a33.png)

运行后：
    
![在这里插入图片描述](https://img-blog.csdnimg.cn/a145d63f7a8a4080a48feba074ad3663.png)
## xml_txt.py
- 代码作用：xml标签格式转换txt标签格式

- 1、修改待修改xml文件夹和目标txt文件夹路径

![在这里插入图片描述](https://img-blog.csdnimg.cn/5f06aa398049420a868e0b5620d21fda.png)

温馨提示：注意，如果读取当前路径的话，前两个路径要修改成相对路径

![在这里插入图片描述](https://img-blog.csdnimg.cn/9cc6003798c244218b9cc62e525a5b2e.png)
- 2、换成待转换xml标签名称所想排顺序的名称序列

![在这里插入图片描述](https://img-blog.csdnimg.cn/e96261180bae483aa56b28d982564829.png)
- 3、运行xml_txt.py

![在这里插入图片描述](https://img-blog.csdnimg.cn/0ed252a7746f4547af14d93d00a6d902.png)

4、结果展示

运行前：
    
![在这里插入图片描述](https://img-blog.csdnimg.cn/dc3ad21e442f483893e37fcd022c8f37.png)

运行后：
    
![在这里插入图片描述](https://img-blog.csdnimg.cn/c058a7b656e94ad5b61db84262ba371c.png)

<span style="color:pink;">Author: MBJC</span>  
<span style="color:pink;">Last modification time: 2022/8/2 19:48</span>
