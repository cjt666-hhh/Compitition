from flask import Flask, request, jsonify

from servicee.CheckPaperService import getOcrAnswer
from servicee import CheckPaperService as cp
app = Flask(__name__)


@app.route('/api/getOcrAnswer', methods=['POST'])
def ocr_answer_api():
    # 从请求中获取数据
    data = request.get_json()

    # 提取所需的参数
    answer_sheet = data.get('answer_sheet')
    templates = data.get('templates',[])
    stu_answer = data.get('stu_answer')

    # 确保所有必要的参数都已提供
    if not all([answer_sheet, templates, stu_answer]):
        return jsonify({'error': 'Missing required parameters'}), 400

        # 调用你的函数并获取结果
    try:
        ocrResults = getOcrAnswer(answer_sheet, templates, stu_answer)
        # 返回结果
        return jsonify(ocrResults)
    except Exception as e:
        # 如果发生错误，返回错误信息
        return jsonify({'error': str(e)}), 500

    # 注意：你需要确保getOcrAnswer函数能正确处理传入的参数类型，


# 比如，如果templates是一个图片地址列表，你可能需要在调用函数之前将其从JSON数组转换成Python列表。
@app.route('/get_comment', methods=['POST'])
def get_comment():
    # 从请求中获取必要的参数
    data = request.json

    # 提取单个值
    answer_sheet = data.get('answer_sheet')
    stu_answer = data.get('stu_answer')

    # 提取列表值
    templates = data.get('templates', [])  # 默认为空列表
    questions = data.get('questions', [])  # 默认为空列表
    princ_answers = data.get('princ_answers', [])  # 默认为空列表

    # 验证输入数据的有效性
    if not all([answer_sheet, stu_answer, templates, questions, princ_answers]):
        return jsonify({'error': 'Missing required parameters'}), 400

        # 如果templates, questions, princ_answers不是列表，则返回错误
    if not isinstance(templates, list) or not isinstance(questions, list) or not isinstance(princ_answers, list):
        return jsonify({'error': 'Parameters must be lists'}), 400

        # 确保questions和princ_answers有相同的长度
    if len(questions) != len(princ_answers):
        return jsonify({'error': 'Questions and principal answers must have the same length'}), 400

        # 调用getComment函数获取评论结果
    try:
        # 假设 getComment 函数能够处理这些参数
        commentResults = cp.getComment(answer_sheet, templates, stu_answer, questions, princ_answers)
    except Exception as e:
        # 异常处理
        return jsonify({'error': str(e)}), 500

        # 返回评论结果
    return jsonify(commentResults)




if __name__ == '__main__':
    app.run(debug=True)