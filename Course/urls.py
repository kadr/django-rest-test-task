from django.urls import path

from .views import CourseView

app_name = "courses"
urlpatterns = [
    path('courses/', CourseView.as_view()),
    path('courses/<int:pk>', CourseView.as_view())
]
