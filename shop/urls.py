from django.urls import path

from . import views

urlpatterns = [
    path('test/', views.TestListView.as_view()),
    path('test/<int:pk>', views.TestListView.as_view())
]