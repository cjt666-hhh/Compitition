import cv2
import numpy as np
from flask import Flask, request, jsonify
from PIL import Image, ImageEnhance, ImageFilter
from io import BytesIO
import base64
app = Flask(__name__)


def cut(answer_sheet_path, template_path):

 answer_sheet = cv2.imread(answer_sheet_path, cv2.IMREAD_GRAYSCALE)
 if answer_sheet is None:
    print("Error loading answer sheet image!")
    exit()

# 读取第一题的模板图像（假设为灰度图）
 template = cv2.imread(template_path, cv2.IMREAD_GRAYSCALE)
 if template is None:
    print("Error loading template image!")
    exit()

# 获取模板的高度和宽度
 h, w = template.shape  # 使用shape属性获取高度和宽度，[:-1]用于去掉通道数（如果是灰度图则不需要，但这样写更通用）

# 进行模板匹配
 res = cv2.matchTemplate(answer_sheet, template, cv2.TM_CCOEFF_NORMED)

# 设置匹配阈值
 threshold = 0
 min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(res)
 top_left = max_loc  # 最大值的位置是模板的左上角在原图上的位置
 print(max_loc)
 print(max_val)
# 找到匹配区域
 loc = np.where(res >= threshold)

# 标记匹配区域并打印坐标
 for pt in zip(*loc[::-1]):  # 注意这里的坐标顺序需要反转
    ttop_left = (pt[0], pt[1])  # 左上角坐标
    bbottom_right = (pt[0] + w, pt[1] + h)  # 右下角坐标
    if(ttop_left==max_loc):
     return ttop_left,w,h
     cv2.rectangle(answer_sheet, top_left, bbottom_right, (0, 0, 255), 2)
    else:
        continue

def getPoint(answer_sheet, templates):
    results = {}  # 创建一个空字典来存储结果
    for index, template in enumerate(templates):  # 使用enumerate来获取模板及其索引
        topLeft, w, h = cut(answer_sheet, template)  # 假设cut函数返回topLeft坐标和宽高
        # 将结果存入字典，使用索引作为键
        results[index]={'topLeft': topLeft, 'size': (w, h)}
    return results


def getOriginAnswer(answer_sheet, templates,stu_answer):
    image_answer_sheet = cv2.imread(answer_sheet)
    image_stu_answer = cv2.imread(stu_answer)

    # 获取图片A的尺寸
    height_answer_sheet, width_answer_sheet = image_answer_sheet.shape[:2]

    # 使用resize函数将图片B调整为图片A的尺寸
    resized_image_stu_answer = cv2.resize(image_stu_answer, (width_answer_sheet, height_answer_sheet))

    # 保存调整尺寸后的图片B
    image = resized_image_stu_answer
    results = {}  # 创建一个空字典来存储结果
    for index, template in enumerate(templates):  # 使用enumerate来获取模板及其索引
        topLeft, w, h = cut(answer_sheet, template)  # 假设cut函数返回topLeft坐标和宽高
        # 将结果存入字典，使用索引作为键
        x,y=topLeft

        #切割出学生答案
        cropped_image = image[y:y + h, x:x + w]

        imagggg=enhance_text_in_image(cropped_image)

        imagg=np.array(imagggg)



        #储存学生答案
        results[index ] = {'topLeft': topLeft, 'size': (w, h),'image':imagg}
    return results

def enhance_text_in_image(image):


    # 使用Pillow进一步处理
    pil_img = Image.fromarray(image)

    # 增强对比度
    enhancer = ImageEnhance.Contrast(pil_img)
    enhanced_contrast = enhancer.enhance(1.5)

    # 应用锐化滤波器
    sharpened = enhanced_contrast.filter(ImageFilter.SHARPEN)

    # 返回处理后的图片对象，而不是保存
    return sharpened

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
def get_base_OriginAnswer(answer_sheet, templates,stu_answer):
    image_answer_sheet = cv2.imread(answer_sheet)
    image_stu_answer = cv2.imread(stu_answer)

    # 获取图片A的尺寸
    height_answer_sheet, width_answer_sheet = image_answer_sheet.shape[:2]

    # 使用resize函数将图片B调整为图片A的尺寸
    resized_image_stu_answer = cv2.resize(image_stu_answer, (width_answer_sheet, height_answer_sheet))

    # 保存调整尺寸后的图片B
    image = resized_image_stu_answer
    results = {}  # 创建一个空字典来存储结果
    for index, template in enumerate(templates):  # 使用enumerate来获取模板及其索引
        topLeft, w, h = cut(answer_sheet, template)  # 假设cut函数返回topLeft坐标和宽高
        # 将结果存入字典，使用索引作为键
        x,y=topLeft

        #切割出学生答案
        cropped_image = image[y:y + h, x:x + w]

        imagggg=enhance_text_in_image(cropped_image)

        imagg=np.array(imagggg)

        base_image=numpy_array_to_base64(imagg)

        #储存学生答案
        results[index ] = {'topLeft': topLeft, 'size': (w, h),'image':base_image}
    return results