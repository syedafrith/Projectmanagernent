"""
URL configuration for TechForingAssessment project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from rest_framework.generics import ListCreateAPIView

from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

from projects.views import TflProjectView, TflProjectListView
from tasks.views import TflTaskListView, TflTaskView, TflCommentListView, TflCommentView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/login/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/users/', include('users.urls')),
    path('api/projects/', TflProjectListView.as_view()),
    path('api/projects/<int:pk>/', TflProjectView.as_view()),
    path('api/projects/<int:pk>/tasks/', TflTaskListView.as_view()),
    path('api/tasks/<int:pk>/', TflTaskView.as_view()),
    path('api/tasks/<int:pk>/comments/', TflCommentListView.as_view()),
    path('api/comments/<int:pk>/', TflCommentView.as_view()),

]