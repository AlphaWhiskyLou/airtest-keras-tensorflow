# airtest-keras-tensorflow
本项目在Airtest开源项目的基础上，对自动测试进行了本质上的升级。利用YoloV3进行目标检测，对截图中的UI控件进行自动检测。

通过调用 #AirtestCore API （https://airtest.readthedocs.io/zh_CN/latest/all_module/airtest.core.api.html）对所检测到的UI控件进行操作。

keras-airetst.py为运行的文件。在进行测试前，需要将训练好的模型的.h5文件放入model_data文件夹中的log子目录，并将分类标签的.txt文件放入model_data文件夹中。
