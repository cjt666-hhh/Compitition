from service import OpencvService as ov
from service import OcrService as os
from service import chatService as cs
def getOcrAnswer(answer_sheet, templates,stu_answer):
    results=ov.getOriginAnswer(answer_sheet, templates,stu_answer)#取出学生答案
    ocrResults={}#初始化空字典
    #挨个识别学生答案
    for index, value in results.items():
        question_image = value['image']
        ocrResults[index+1]=os.ocr_to_Chi(question_image)
    return ocrResults

def getComment(answer_sheet, templates,stu_answer,questions,princ_answers):
    results=ov.getOriginAnswer(answer_sheet, templates,stu_answer)#取出学生答案
    commentResults={}#初始化空字典

    #挨个识别学生答案
    for index, value in results.items():
        question_image = value['image']
        stu_ans=os.ocr_to_Chi(question_image)
        commentResults[index+1]=cs.chat(stu_ans,princ_answers[index],questions[index])

    return commentResults
