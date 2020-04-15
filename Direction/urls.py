from django.urls import path

from .views import DirectionView

app_name = "directions"
urlpatterns = [
    path('directions/', DirectionView.as_view()),
    path('directions/<int:pk>', DirectionView.as_view())
]
