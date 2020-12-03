from django.urls import path
from . import views
from .views import all_courses, Find_Date_Beginnings_VieData, CreateVieAll, Find_Name_VieData, DeteilView

urlpatterns = [
    path('', views.all_courses),
    path('find_date_beginnings/', Find_Date_Beginnings_VieData.as_view()),
    path('find_name/', Find_Name_VieData.as_view()),
    path('all/', CreateVieAll.as_view()),
    path('deteil/<int:pk>', DeteilView.as_view()),
]
