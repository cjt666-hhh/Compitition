import erniebot

erniebot.api_type = 'aistudio'
erniebot.access_token = '79f46db01a793f00edbb51fe0f3ef223b273fba1'


def chat(stu_answer, princ_answer, ques):
    try:
        response = erniebot.ChatCompletion.create(
            model='ernie-3.5',
            messages=[
                {
                    'role': 'user',
                    'content': "请问你是谁？"
                },
                {
                    'role': 'assistant',
                    'content': "我是百度公司开发的人工智能语言模型，我的中文名是文心一言，英文名是ERNIE-Bot，可以协助您完成范围广泛的任务并提供有关各种主题的信息，比如回答问题，提供定义和解释及建议。如果您有任何问题，请随时向我提问。"
                },
                {
                    'role': 'user',
                    'content': f"能不能帮我评价一下学生作答情况,不需要评价标准答案，只需要评价学生答案，原题是{ques}，学生的答案是{stu_answer}，标准答案是{princ_answer}"
                }
            ]
        )
        result = response.get_result()  # 假设这个方法返回一个包含结果的字典或其他对象
        # 这里需要根据实际的返回结构来提取润色后的评语
        # 假设润色后的评语直接作为字符串返回，但这通常不太可能，需要根据实际情况调整
        return result  # 这里可能需要进一步处理result来获取真正的润色后的评语
    except Exception as e:
        # 在生产环境中，应该记录错误而不是仅仅打印出来
        print(f"An error occurred: {e}")
        return None

    # 示例调用（请替换为您自己的参数）


