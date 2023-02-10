from django.urls import path
from . import views

urlpatterns = [
    path('watch/<int:pk>', views.WatchVideoAPIView.as_view()),
    path('upload/')
    # path('upload/')
]

