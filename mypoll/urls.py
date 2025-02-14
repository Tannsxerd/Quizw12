from django.urls import path

from . import views

app_name = "mypoll"

urlpatterns = [
    path("",views.index,name = "index"),
    path("mypoll/<int:question_id>/",views.detail,name = "detail"),
    path("mypoll/<int:question_id>/vote/",views.vote,name = "vote"),
    path("mypoll/<int:question_id>/results/",views.results,name = "results"),
]