from django.urls import path

from .views import LessonView, LessonMaterialView

app_name = "lessons"
urlpatterns = [
    path('lessons/', LessonView.as_view()),
    path('lessons/<int:pk>', LessonView.as_view()),
    path('lessons-material/', LessonMaterialView.as_view()),
    path('lessons-material/<int:pk>', LessonMaterialView.as_view())
]
