from django.urls import path
from .views import FootballClubListView,FootballClubDetailView,footballclub_create,footballclub_update,footballclub_delete, RegisterAPIView,ProfileAPIView,LogoutAPIView
from rest_framework_simplejwt.views import(TokenObtainPairView, TokenRefreshView)

urlpatterns=[
    path("FootballClubs/",FootballClubListView),
    path("FootballClubs/create",footballclub_create),
    path("FootballClubs/<int:pk>/",FootballClubDetailView),
    path("FootballClubs/update/<int:pk>",footballclub_update),
    path("FootballClubs/delete/<int:pk>",footballclub_delete),
    path("register/",RegisterAPIView.as_view()),
    path("Profile/",ProfileAPIView.as_view()),
    path("logout/",LogoutAPIView.as_view()),
    path("login/",TokenObtainPairView.as_view()),
    path("refresh/",TokenRefreshView.as_view()),
]