from django.shortcuts import render
from .models import FootballClub
from rest_framework import viewsets
from .serializers import FootballClubSerializer
from rest_framework.generics import ListAPIView, CreateAPIView, RetrieveAPIView, UpdateAPIView, DestroyAPIView, RetrieveUpdateAPIView, RetrieveDestroyAPIView, RetrieveUpdateDestroyAPIView

class FootballClubListAPIView(ListAPIView):
    queryset=FootballClub.objects.all()
    serializer_class=FootballClubSerializer

class FootballClubCreateAPIView(CreateAPIView):
    queryset=FootballClub.objects.all()
    serializer_class=FootballClubSerializer
    
class FootballClubRetrieveAPIView(RetrieveAPIView):
    queryset=FootballClub.objects.all()
    serializer_class=FootballClubSerializer
    
class FootballClubUpdateAPIView(UpdateAPIView):
    queryset=FootballClub.objects.all()
    serializer_class=FootballClubSerializer
    
class FootballClubDestroyAPIView(DestroyAPIView):
    queryset=FootballClub.objects.all()
    serializer_class=FootballClubSerializer

class FootballClubRetrieveUpdateAPIView(RetrieveUpdateAPIView):
    queryset=FootballClub.objects.all()
    serializer_class=FootballClubSerializer
    
class FootballClubRetrieveDestroyAPIView(RetrieveDestroyAPIView):
    queryset=FootballClub.objects.all()
    serializer_class=FootballClubSerializer
    
class FootballClubRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    queryset=FootballClub.objects.all()
    serializer_class=FootballClubSerializer
    
