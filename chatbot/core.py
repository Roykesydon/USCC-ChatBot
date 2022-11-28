import re
import long_responses as long
import jieba
from .qa_data import qa_data

jieba.set_dictionary('dict.txt.big')

def message_probability(user_message, recognised_words, required_words=[]):
    message_certainty = 0
    has_required_words = True

    # 數有多少個詞出現在預設問句中
    for word in user_message:
        if word in recognised_words:
            message_certainty += 1

    # 計算比例
    # percentage = float(message_certainty) / float(len(recognised_words))

    # 確認必須出現的詞在不在使用者的問句中
    for word in required_words:
        if word not in user_message:
            has_required_words = False
            break

    if not has_required_words:
        return 0
    else:
        # return int(percentage * 100)
        return message_certainty


def check_all_messages(message):
    highest_prob_list = {}

    # 計算預設問句和 message 的相似比例
    def response(bot_response, list_of_words, required_words=[]):
        nonlocal highest_prob_list
        highest_prob_list[bot_response] = message_probability(message, list_of_words, required_words)

    # 預設問答集
    for qa in qa_data:
        print(qa)
        response(qa["answer"], qa["query_words"], qa["require_words"])

    best_match = max(highest_prob_list, key=highest_prob_list.get)
    # print(highest_prob_list)
    # print(f'Best match = {best_match} | Score: {highest_prob_list[best_match]}')

    if highest_prob_list[best_match] == 0:
        return "抱歉我不太懂"
    else:
        return best_match
    


# 回傳答案
def get_response(question:str) -> str:
    print(question)
    split_message = list(jieba.cut(question, cut_all=False, HMM=True))
    print('|'.join(split_message))
    response = check_all_messages(split_message)
    return response