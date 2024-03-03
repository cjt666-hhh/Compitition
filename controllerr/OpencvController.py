from flask import Flask, request, jsonify

from service.OpencvService import getOriginAnswer

app = Flask(__name__)
@app.route('/get_origin_answer', methods=['POST'])
def get_origin_answer():

    data = request.json
    answer_sheet = data.get('answer_sheet')
    templates = data.get('templates', [])
    stu_answer = data.get('stu_answer')

    if not answer_sheet or not stu_answer or not templates:
        return jsonify({'error': 'Missing required parameters'}), 400

    # 调用getOriginAnswer函数并获取结果
    try:
        results = getOriginAnswer(answer_sheet, templates, stu_answer)
    except Exception as e:
        return jsonify({'error': str(e)}), 500

    # 返回结果
    return jsonify(results)




if __name__ == '__main__':
    app.run(debug=True)