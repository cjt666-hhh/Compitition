from flask import Flask, request, jsonify
from paddleocr import PaddleOCR, draw_ocr
from PIL import Image
import numpy as np


app = Flask(__name__)
ocr = PaddleOCR(use_angle_cls=True, lang="en")


@app.route('/ocr', methods=['POST'])
def ocr_endpoint():
    if 'file' not in request.files:
        return jsonify({'error': 'No file part in the request'}), 400

    file = request.files['file']
    if file.filename == '':
        return jsonify({'error': 'No selected file'}), 400

        # 使用 PIL 库从上传的文件中读取图片，并转换为 NumPy 数组
    image = Image.open(file.stream)
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
    return jsonify({'result': ocr_output})


if __name__ == '__main__':
    app.run(debug=True)