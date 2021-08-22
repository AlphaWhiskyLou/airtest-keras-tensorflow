import random
from PIL import Image, ImageEnhance
import os

src_path = '/home/lou/keras-yolo3/add_img/'

dst_path1 = '/home/lou/keras-yolo3/enhancement_brightness/'
dst_path2 = '/home/lou/keras-yolo3/enhancement_color/'
dst_path21 = '/home/lou/keras-yolo3/enhancement_color_/'
dst_path3 = '/home/lou/keras-yolo3/enhancement_contrast/'
dst_path31 = '/home/lou/keras-yolo3/enhancement_contrast_/'
dst_path4 = '/home/lou/keras-yolo3/enhancement_sharpness/'
dst_path41 = '/home/lou/keras-yolo3/enhancement_sharpness_/'
"""
dst_path1 = '/home/lou/keras-yolo3/enhancement+/'
dst_path2 = '/home/lou/keras-yolo3/enhancement+/'
dst_path21 = '/home/lou/keras-yolo3/enhancement+/'
dst_path3 = '/home/lou/keras-yolo3/enhancement+/'
dst_path31 = '/home/lou/keras-yolo3/enhancement+/'
dst_path4 = '/home/lou/keras-yolo3/enhancement+/'
dst_path41 = '/home/lou/keras-yolo3/enhancement+/'
"""
filelist=os.listdir(src_path)

for img in filelist:
    image = Image.open(src_path + img)
    img_bright = ImageEnhance.Brightness(image)
    image = img_bright.enhance(0.9)
    image.save(dst_path1 + 'b' +img)

for img in filelist:
    image = Image.open(src_path + img)
    img_bright = ImageEnhance.Color(image)
    image = img_bright.enhance(1.5)
    image.save(dst_path2 + 'col' + img)
for img in filelist:
    image = Image.open(src_path + img)
    img_bright = ImageEnhance.Color(image)
    image = img_bright.enhance(0.5)
    image.save(dst_path21 + 'coll' + img)

for img in filelist:
    image = Image.open(src_path + img)
    img_bright = ImageEnhance.Contrast(image)
    image = img_bright.enhance(1.2)
    image.save(dst_path3 + 'con' + img)
for img in filelist:
    image = Image.open(src_path + img)
    img_bright = ImageEnhance.Contrast(image)
    image = img_bright.enhance(0.5)
    image.save(dst_path31 + 'conn' + img)

for img in filelist:
    image = Image.open(src_path + img)
    img_bright = ImageEnhance.Sharpness(image)
    image = img_bright.enhance(3.0)
    image.save(dst_path4 + 's' + img)
for img in filelist:
    image = Image.open(src_path + img)
    img_bright = ImageEnhance.Sharpness(image)
    image = img_bright.enhance(0.5)
    image.save(dst_path41 + 'ss' + img)
