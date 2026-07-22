from django.urls import path
from .views import FootballClubListView,FootballClubDetailView,footballclub_create,footballclub_update,footballclub_delete
from . import views

urlpatterns=[
    path("FootballClubs/",FootballClubListView),
    path("FootballClubs/create",footballclub_create),
    path("FootballClubs/<int:pk>/",FootballClubDetailView),
    path("FootballClubs/update/<int:pk>",footballclub_update),
    path("FootballClubs/delete/<int:pk>",footballclub_delete),
]