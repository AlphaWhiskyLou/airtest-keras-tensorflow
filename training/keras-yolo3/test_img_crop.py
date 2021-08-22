# 引入模块
from PIL import Image

path = '/home/talisman/keras-yolo3/55.jpg'
def cut_img(path):
    # 读取原图
    img = Image.open(path)
    print(img.size)

    # 图片剪切crop(x,y,x1,y1)
    im = img.crop((0,0,1080,1170))
    print(im.size)

    # 保存剪切出来的图片
    cut_name = '/home/talisman/keras-yolo3/pt1.jpg'
    im.save(cut_name)

    # 图片剪切crop(x,y,x1,y1) left, upper, right, and lower
    im = img.crop((0, 1170, 1080, 2340))
    print(im.size)

    # 保存剪切出来的图片
    cut_name = '/home/talisman/keras-yolo3/pt2.jpg'
    im.save(cut_name)

cut_img(path)