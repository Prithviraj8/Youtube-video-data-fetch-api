from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import filters
from django_filters.rest_framework import DjangoFilterBackend

from .models import VideoInformation
from .serializers.serializers import YoutubeVideoFetchSerializer

# Rest FrameWork
from rest_framework import generics
from rest_framework.pagination import CursorPagination

from youtube_video_fetch_api.operations import youtube_videos

class ResultsPagination(CursorPagination):
    page_size = 25
    page_size_query_param = 'page_size'
    max_page_size = 100


# Searching is implemented using DRF Filters
# DRF filter by default uses [icontains] and thus the search by default supports partial searches

class YoutubeVideoFetchViewSet(generics.ListAPIView):
    filterset_fields = ['channel_id', 'channel_title']
    ordering = ('-publishedAt')
    queryset = VideoInformation.objects.all()
    serializer_class = YoutubeVideoFetchSerializer
    pagination_class = ResultsPagination

    def list(self, request, *args, **kwargs):
        video_title = request.query_params.dict()['title']
        try:
            result = youtube_videos.youtube_search(video_title)
        except Exception as e:
            return Response({"Error ": e})
        return Response({"results :": result})
