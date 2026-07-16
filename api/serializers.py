from rest_framework.serializers import ModelSerializer
from .models import FootballClub

class FootballClubSerializer(ModelSerializer):
    class Meta:
        model=FootballClub
        fields=["id","nomi","sovrinlar","murabbiy","stadion","tashkl_topgan_yili","created_at"]
        read_only_fields=["id","created_at"]