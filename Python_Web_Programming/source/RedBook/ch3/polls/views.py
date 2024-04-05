from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect
from django.urls import reverse

from polls.models import Choice, Question


def index(request):
    latest_question_list = Question.objects.all().order_by("-pub_date")[:5]
    context = {"latest_question_list": latest_question_list}
    return render(request, "polls/index.html", context)


def detail(request, question_id):
    question = get_object_or_404(
        Question, pk=question_id
    )  # model class, 검색 조건, 조건에 맞는 객체가 없으면 HTTP404 error
    return render(
        request, "polls/detail.html", {"question": question}
    )  # 사용자에게 보여줄 최종 html을 담아서 HttpResponse 객체를 반환


def results(request, question_id):  # request는 필수 인자
    question = get_object_or_404(Question, pk=question_id)
    return render(request, "polls/results.html", {"question": question})


def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(
            pk=request.POST["choice"]
        )  # choice table을 검색, 키가 choice에 해당하는 값인 choice.id 리턴
    except (KeyError, Choice.DoesNotExist):
        # Redisplay the question voting form.
        return render(
            request,
            "polls/detail.html",
            {
                "question": question,
                "error_message": "You didn't select a choice.",
            },
        )  # exception 발생
    else:
        selected_choice.votes += 1  # count 증가
        selected_choice.save()  # 저장
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
        return HttpResponseRedirect(
            reverse("polls:results", args=(question.id,))
        )  # 결과 반환
