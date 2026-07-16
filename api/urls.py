from django.urls import path
from .views import FootballClubListAPIView
from . import views

urlpatterns=[
    path("FootballClub/",views.FootballClubListAPIView.as_view(), name="FootballClub-list"),
    path("FootballClub/create",views.FootballClubCreateAPIView.as_view(), name="FootballClub-create"),
    path("FootballClub/<int:pk>/",views.FootballClubRetrieveAPIView.as_view(), name="FootballClub-detail"),
    path("FootballClub/update/<int:pk>",views.FootballClubUpdateAPIView.as_view(), name="FootballClub-update"),
    path("FootballClub/delete/<int:pk>",views.FootballClubDestroyAPIView.as_view(), name="FootballClub-delete"),
    path("FootballClub/detail-update/<int:pk>",views.FootballClubRetrieveUpdateAPIView.as_view(), name="FootballClub-detail-update"),
    path("FootballClub/detail-delete/<int:pk>",views.FootballClubRetrieveDestroyAPIView.as_view(), name="FootballClub-detail-delete"),
    path("FootballClub/<int:pk>/manager/",views.FootballClubRetrieveUpdateDestroyAPIView.as_view(), name="FootballClub-manager"),
]