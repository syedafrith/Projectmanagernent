from django.urls import path

from users.views import TflUserRegisterView, TflUserView

urlpatterns = [
    path('register/',TflUserRegisterView.as_view()),
    path('<int:pk>/',TflUserView.as_view()),

]