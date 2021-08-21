# airtest-keras-tensorflow
本项目在Airtest开源项目的基础上，对自动测试进行了本质上的升级。利用YoloV3进行目标检测，对截图中的UI控件进行自动检测。

通过调用 AirtestCore API （https://airtest.readthedocs.io/zh_CN/latest/all_module/airtest.core.api.html）对所检测到的UI控件进行操作。

keras-airetst.py为运行的文件。在进行测试前，需要将训练好的模型的.h5文件放入model_data文件夹中的log子目录，并将分类标签的.txt文件放入model_data文件夹中。

项目文件结构介绍：

原型工具文件夹：包含了运行工具所需要的核心文件夹keras_test.air，以及包含了目标检测模型和运行目标检测所需要的文件的model_data文件夹。

模型训练相关文件夹：包含了训练目标检测模型所需要的相关文件，包括了数据增强脚本，数据集划分脚本等，但是由于文件大小限制，已经将所有的数据集图像删除。

工具运行的具体方法：

1. 在Ubuntu系统下利用keras.yml配置项目所需要的环境（推荐利用anaconda）
2. 激活项目运行环境
3. 连接被测试设备，打开USB调试模式并将被测试设备调整到待测试的页面
4. 进入原型工具文件夹
   - 若不需要更换目标检测的权重模型，则可忽略以下步骤，直接进行第5步
   - 如果需要使用其它目标检测的模型权重，首先进入model_data文件夹
   - 将my_class.txt中的标签替换为新的标签
   - 若需要使用自定义的锚点，可更改yolo_anchor.txt
   - 进入logs子目录
   - 用新的模型权重的.h5文件替换原来的文件
   - 若文件名有更改，还需要对应地更改keras_test.py文件中YOLO类下的'model_path'处的对应名称
5. 输入运行指令（例如：airtest run keras_test.air --device Android://127.0.0.1:5037/<adb devices中可以查看的设备号>）
6. 开始自动测试
