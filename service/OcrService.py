from flask import jsonify
from paddleocr import PaddleOCR, draw_ocr
from PIL import Image
import numpy as np


def ocr_to_eng(image_path):
    # 初始化 PaddleOCR
    ocr = PaddleOCR(use_angle_cls=True, lang="en")

    # 读取图片
    try:
        image = Image.open(image_path)
    except FileNotFoundError:
        return jsonify({'error': 'File not found'}), 404

        # 将图片转换为 NumPy 数组
    img_array = np.array(image)

    # 进行 OCR 识别
    result = ocr.ocr(img_array, cls=True)

    # 格式化 OCR 结果
    ocr_output = []
    for idx in range(len(result)):
        res = result[idx]
        for line in res:
            ocr_output.append(line[1][0])  # 添加识别出的文本内容到输出列表

    # 返回 OCR 结果
    return {'result': ocr_output}

def ocr_to_Chi(image):
    # 初始化 PaddleOCR
    ocr = PaddleOCR(use_angle_cls=True, lang="ch")

    # 读取图片

        # 将图片转换为 NumPy 数组
    img_array = np.array(image)

    # 进行 OCR 识别
    result = ocr.ocr(img_array, cls=True)

    # 格式化 OCR 结果
    ocr_output = []
    for idx in range(len(result)):
        res = result[idx]
        for line in res:
            ocr_output.append(line[1][0])  # 添加识别出的文本内容到输出列表

    # 返回 OCR 结果
    return {'result': ocr_output}


