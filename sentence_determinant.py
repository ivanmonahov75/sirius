from sentence_transformers import SentenceTransformer, util
from time import *
from faq import *


class SentenceDeterminant:
    model = SentenceTransformer('all-MiniLM-L6-v2')
    questions = list(QUESTIONS.keys())
    embeddings = model.encode(questions)

    def __init__(self):
        if not SentenceDeterminant.model:
            SentenceDeterminant.model = SentenceTransformer('all-MiniLM-L6-v2')
            questions = []
            # for question in FAQ.all():
            #     questions.append(question.title_ru)
            #     SentenceDeterminant.answers.append(question.answer_ru)
            # SentenceDeterminant.embeddings = SentenceDeterminant.model.encode(questions)

    def get_closest_question(self, sentence):
        emb = SentenceDeterminant.model.encode(sentence)
        cos_sim = util.cos_sim(SentenceDeterminant.embeddings, [emb])
        sentence_combinations = []
        for i in range(0, len(cos_sim)):
            sentence_combinations.append([i, cos_sim[i]])
        sentence_combinations = sorted(sentence_combinations, key=lambda x: x[1], reverse=True)
        if sentence_combinations[0][1] < 0.6:
            return 'я не могу ответить правильно'
        return ANSWERS[QUESTIONS[SentenceDeterminant.questions[sorted(sentence_combinations, key=lambda x: x[1], reverse=True)[0][0]]]]
