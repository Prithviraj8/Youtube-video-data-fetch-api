from rest_framework import serializers


class YoutubeVideoFetchSerializer(serializers.Serializer):
    video_title = serializers.CharField(required=True)
