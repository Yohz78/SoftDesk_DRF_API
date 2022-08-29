from django.urls import path

from . import views

urlpatterns = [
    path("", views.ProjectListCreateAPIView.as_view()),
    path("<int:pk>/", views.ProjectDetailAPIView.as_view()),
    path("<int:pk>/delete/", views.ProjectRetrieveDestroyAPIView.as_view()),
    path("<int:pk>/update/", views.ProjectRetrieveUpdateAPIView.as_view()),
]
