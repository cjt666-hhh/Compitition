import erniebot

erniebot.api_type = 'aistudio'
erniebot.access_token = '79f46db01a793f00edbb51fe0f3ef223b273fba1'
msgg="学生表现良好"

from flask import Flask, request, jsonify


app = Flask(__name__)


@app.route('/chat', methods=['POST'])
def chat_api():
    msgg = request.json.get('msgg', '')  # 从POST请求的JSON中获取'msgg'字段
    if not msgg:
        return jsonify({'error': 'Missing "msgg" parameter in the request body.'}), 400

        # 调用chat函数并获取结果
    try:
        response = erniebot.ChatCompletion.create(
            model='ernie-3.5',
            messages=[{
                'role': 'user',
                'content': "请问你是谁？"
            }, {
                'role': 'assistant',
                'content': "我是百度公司开发的人工智能语言模型，我的中文名是文心一言，英文名是ERNIE-Bot，可以协助您完成范围广泛的任务并提供有关各种主题的信息，比如回答问题，提供定义和解释及建议。如果您有任何问题，请随时向我提问。"
            }, {
                'role': 'user',
                'content': "能不能帮我润色一下学生评语？我的评语是" + msgg+"，只输出润色后的学生评语"
            }])
        result = response.get_result()  # 假设get_result()方法返回的是润色后的评语或其他响应
    except Exception as e:
        return jsonify({'error': str(e)}), 500

        # 返回结果
    return jsonify(result)


if __name__ == '__main__':
    app.run(debug=True)