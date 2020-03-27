from radio.models import Hits, Artists
from rest_framework import serializers


class ArtistSerializer(serializers.ModelSerializer):
    class Meta:
        model = Artists
        fields = ['pk', 'first_name', 'last_name']


class HitsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Hits
        fields = ['pk', 'title', 'title_url']


class CreateHitsSerializer(serializers.ModelSerializer):

    class Meta:
        model = Hits
        fields = ['title', 'title_url', 'artist_id']


class UpdateHitsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Hits
        fields = ['title', 'title_url', 'artist_id']


class HitsDetailsSerializer(serializers.ModelSerializer):
    artist_id = ArtistSerializer()

    class Meta:
        model = Hits
        fields = ['pk', 'title', 'title_url', 'created_at', 'artist_id']
