from django.urls import path

from . import views

app_name = "polls"

# todas las URLS que cuelgan de localhost:8000/polls/
urlpatterns = [
    # /polls/
    path("", views.index, name="index"),

    # /polls/question-detail/5/
    path("question-detail/<int:question_id>/", views.detail, name="detail"),

    # /polls/5/results/
    path("<int:question_id>/results/" , views.results, name="results"),

    # /polls/5/vote/
    path("<int:question_id>/vote/", views.vote, name="vote"),
]