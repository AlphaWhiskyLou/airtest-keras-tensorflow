[2]#推荐的resize并存储的方法如下

'''
1、我们将搜集到的图片存放在与软件脚本同一根目录下的'./data/image/pre_train/'文件夹下；
2、我们使用Image模块从pre_train文件夹读取图片，resize，并存储入'./data/image/train/'文件夹；
'''

from PIL import Image
from yolo3.utils import letterbox_image
import os

src_path = '/home/talisman/keras-yolo3/resize_full_in/'
dst_path = '/home/talisman/keras-yolo3/resize_full_out/'

filelist=os.listdir(src_path)

for img in filelist:
    image = Image.open(src_path + img)
    boxed_image = letterbox_image(image, tuple((416,416)))
    #boxed_image.show()
    boxed_image.save(dst_path + img)


    """
    from PIL import Image
    image=Image.open("1.jpg")
    image = image.convert('RGB')
    w, h = image.size
    background = Image.new('RGB', size=(max(w, h), max(w, h)), color=(127, 127, 127))  # 创建背景图，颜色值为127
    length = int(abs(w - h) // 2)  # 一侧需要填充的长度
    box = (length, 0) if w < h else (0, length)  # 粘贴的位置
    background.paste(image, box)
    image_data=background.resize((256,256))#缩放
    background.show()



    image=Image.open(src_path+img)
    w, h = image.size
    background = Image.new('RGB', size=(max(w, h), max(w, h)), color=(255, 255, 255))  #white is (255,255,255), black is (0,0,0)
    length = int(abs(w - h) // 2)
    box = (length, 0) if w < h else (0, length)
    background.paste(image, box)
    image_resize=background.resize((416,416))
    #image.resize(size,resample=0)  #sesam用于表示改变图像过程中的插值方法，0：双线性插值；1：最邻近插值；2：双三次插值；3|面积插值法
    #参考：python: PIL的Image.resize()函数：
    image_resize.save(dst_path+img)
    
            if self.model_image_size != (None, None):
            assert self.model_image_size[0]%32 == 0, 'Multiples of 32 required'
            assert self.model_image_size[1]%32 == 0, 'Multiples of 32 required'
            boxed_image = letterbox_image(image, tuple(reversed(self.model_image_size)))
        else:
            new_image_size = (image.width - (image.width % 32),
                              image.height - (image.height % 32))
            boxed_image = letterbox_image(image, new_image_size)
        image_data = np.array(boxed_image, dtype='float32')
        print(image_data.shape) #print image shape
        boxed_image.show()
    """
