from django.contrib import admin
from django.urls import path
from polls import views

"""
route: URL pattern을 표현하는 문자열
view: URL string이 매칭되면 호출하는 view 함수. HttpRequest 객체와 URL string에서 추출된 항목이 view 함수 인자로 전달.
kwargs: URL string에서 추출된 항목 되에 추가적인 인자를 view 함수에 전달할 때, python dict type으로 인자를 정의.
name: 각 URL pattern별로 이름을 정한다. 여기서 정한 이름은 template 파일에서 많이 사용.
"""

"""
path에 polls/ 가 빠진 이유는 app_name을 polls 라고 지정했기 때문
"""
app_name = "polls"  # namespace 같은 역할을 한다.
urlpatterns = [
    path("admin/", admin.site.urls),
    path("", views.index, name="index"),  # /polls/
    path("<int:question_id>/", views.detail, name="detail"),  # /polls/5/
    path(
        "<int:question_id>/results/", views.results, name="results"
    ),  # /polls/5/results/
    path("<int:question_id>/vote/", views.vote, name="vote"),  # /polls/5/vote/
]
