#from lib.db_connector import DBConnector


class FAQ:
    def __init__(self, id, title_ru, title_en, answer_ru, answer_en):
        self.id = id
        self.title_ru = title_ru
        self.title_en = title_en
        self.answer_ru = answer_ru
        self.answer_en = answer_en

    @staticmethod
    def all():
        faq = []
        results = DBConnector.execute("""SELECT * FROM faq""")
        for question in results:
            faq.append(FAQ(question[0], question[1], question[2], question[3], question[4]))
        return faq

    @staticmethod
    def find_by_id(id):
        result = DBConnector.execute(f"""SELECT * FROM faq WHERE id = {id}""")
        question = result.fetchone()
        return FAQ(question[0], question[1], question[2], question[3], question[4])

    @staticmethod
    def find_by_title_en(title_en):
        result = DBConnector.execute("""SELECT * FROM faq WHERE title_en = %(title_en)s""", {'title_en': title_en})
        question = result.fetchone()
        return FAQ(question[0], question[1], question[2], question[3], question[4])

    def save(self):
        DBConnector.execute_commit(
            """UPDATE faq SET 
                title_ru = %(title_ru)s,
                title_en = %(title_en)s,
                answer_ru = %(answer_ru)s,
                answer_en = %(answer_en)s
                WHERE id = %id)s""",
            {'title_ru': self.title_ru,
             'title_en': self.title_en,
             'answer_ru': self.answer_ru,
             'answer_en': self.answer_en,
             'id': self.id})

    @staticmethod
    def create(title_ru, title_en, answer_ru, answer_en):
        DBConnector.execute_commit(
            """INSERT INTO users  ( title_ru, title_en, answer_ru, answer_en)
                            VALUES( %(title_ru)s, 
                                    %(title_en)s, 
                                    %(answer_ru)s,
                                    %(answer_en)s""",
            {'title_ru': title_ru,
             'title_en': title_en,
             'answer_ru': answer_ru,
             'answer_en': answer_en,})
        return FAQ.find_by_title_en(title_en)

    def destroy(self):
        DBConnector.execute_commit("""DELETE FROM users WHERE chat_id = %(chat_id)s""", {'chat_id': self.chat_id})
