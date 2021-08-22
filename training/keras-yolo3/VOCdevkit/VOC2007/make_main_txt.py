# #完成所有熊猫照片的标注后，还要将数据集划分下训练集、测试集和验证集。
# 在github上下载一个自动划分的脚本（https://github.com/EddyGao/make_VOC2007/blob/master/make_main_txt.py）
# 然后执行以下代码
# python make_main_txt.py
# 将会按照脚本里面设置的比例，自动拆分训练集、测试集和验证集，将相应的文件名列表保存在里面
import os
import random

trainval_percent = 0.66
train_percent = 0.79
xmlfilepath = '/home/lou/keras-yolo3/VOCdevkit/VOC2007/Annotations'
txtsavepath = '/home/lou/keras-yolo3/VOCdevkit/VOC2007/ImageSets'
total_xml = os.listdir(xmlfilepath)

num = len(total_xml)
list = range(num)
tv = int(num * trainval_percent)
tr = int(tv * train_percent)
trainval = random.sample(list, tv)
train = random.sample(trainval, tr)

ftrainval = open('/home/lou/keras-yolo3/VOCdevkit/VOC2007/ImageSets/Main/trainval.txt', 'w')
ftest = open('/home/lou/keras-yolo3/VOCdevkit/VOC2007/ImageSets/Main/test.txt', 'w')
ftrain = open('/home/lou/keras-yolo3/VOCdevkit/VOC2007/ImageSets/Main/train.txt', 'w')
fval = open('/home/lou/keras-yolo3/VOCdevkit/VOC2007/ImageSets/Main/val.txt', 'w')

for i in list:
    name = total_xml[i][:-4] + '\n'
    if i in trainval:
        ftrainval.write(name)
        if i in train:
            ftrain.write(name)
        else:
            fval.write(name)
    else:
        ftest.write(name)

ftrainval.close()
ftrain.close()
fval.close()
ftest.close() 
