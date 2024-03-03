from service import OpencvService as ov
from servicee import CheckPaperService as cp
import cv2
from service import chatService as cs
import numpy as np
from PIL import Image
from io import BytesIO
import base64
answer_sheet='C:/Users/LENOVO/Desktop/python/3f70b82f-f7c5-495a-9b3a-b4b3d019a9b91.gif'
temp_1="D:/python/codingnote/compitition/imggs/img_1.png"
templates=[temp_1]

cv2.imread(answer_sheet)
cv2.imread(temp_1)
result=ov.getOriginAnswer(answer_sheet,templates,answer_sheet)
# 假设你有一个NumPy数组 `image_array`，它代表了一张图片
# 例如: image_array = np.random.randint(0, 256, (height, width, 3), dtype=np.uint8)
image_array = result[0]['image']
# 使用Pillow将NumPy数组转换为图像对象
def numpy_array_to_base64(image_array):

    image = Image.fromarray(image_array)

    # 创建一个BytesIO对象，用于在内存中保存图像数据
    image_io = BytesIO()

    # 将图像保存到BytesIO对象中，格式为PNG（你也可以选择JPEG等其他格式）
    image.save(image_io, format='PNG')

    # 获取BytesIO对象中的图像数据，并转换为Base64编码
    image_base64 = base64.b64encode(image_io.getvalue()).decode('utf-8')

    # 返回Base64编码的图像数据
    return image_base64


print(ov.getOriginAnswer(answer_sheet,templates,answer_sheet))


