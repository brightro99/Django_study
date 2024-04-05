from django.db import models

"""
Django는 항상 PK에 대한 속성을 Not Null 및 Autoincrement로 이름은 id로 해서 자동으로 만들어준다.
FK는 _id 라는 접미사를 붙여서 명칭을 지정하자.
"""


class Question(models.Model):
    """
    id, integer, (id), (PK는 Django에서 자동생성)
    question_text, varchar(200), question_text, models.CharField(max_length=200)
    pub_date, datetime, pub_date, models.DateTimeField('date published')
    """

    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField("date published")

    def __str__(self):  # 객체를 문자열로 표현할 때 쓰이는 함수
        return self.question_text


class Choice(models.Model):
    """
    id, integer, (id), (PK는 Django에서 자동생성)
    choice_text, varchar(200), choice_text, models.CharField(max_length=200)
    votes, integer, votes, models.IntegerField(default=0)
    question_id, integer, question, models.ForeignKey(Question)
    """

    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    def __str__(self):
        return self.choice_text
