from sentence_transformers import SentenceTransformer, util

from faq import FAQ


class SentenceDeterminant:
    model = None
    embeddings = None
    answers = []

    def __init__(self):
        if not SentenceDeterminant.model:
            SentenceDeterminant.model = SentenceTransformer('all-MiniLM-L6-v2')
            questions = []
            for question in FAQ.all():
                questions.append(question.title_ru)
                SentenceDeterminant.answers.append(question.answer_ru)
            SentenceDeterminant.embeddings = SentenceDeterminant.model.encode(questions)

    def get_closest_question(self, sentence):
        emb = SentenceDeterminant.model.encode(sentence)
        cos_sim = util.cos_sim(SentenceDeterminant.embeddings, [emb])
        sentence_combinations = []
        for i in range(0, len(cos_sim)):
            sentence_combinations.append([i, cos_sim[i]])
        return SentenceDeterminant.answers[sorted(sentence_combinations, key=lambda x: x[1], reverse=True)[0][0]]
