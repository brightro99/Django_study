from django.contrib import admin
from polls.models import Question, Choice

# site에 class 등록
admin.site.register(Question)
admin.site.register(Choice)
