from rest_framework import serializers
from youtube_video_fetch_api.models import VideoInformation


class YoutubeVideoFetchSerializer(serializers.ModelSerializer):
    class Meta:
        model = VideoInformation
        fields = ("title", "channel")
