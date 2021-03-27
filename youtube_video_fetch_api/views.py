from rest_framework.response import Response
from .serializers.serializers import YoutubeVideoFetchSerializer

# Rest FrameWork
from rest_framework.viewsets import GenericViewSet
from rest_framework.pagination import CursorPagination

# Model
from youtube_video_fetch_api.operations import youtube_videos


class ResultsPagination(CursorPagination):
    page_size = 25
    page_size_query_param = 'page_size'
    max_page_size = 100


class YoutubeVideoFetchViewSet(generics.ListAPIView):

    def list(self, request, **kwargs):
        serializer = YoutubeVideoFetchSerializer(data=request.query_params.dict())
        serializer.is_valid(raise_exception=True)
        video_title = serializer.validated_data['video_title']

        try:
            result = youtube_videos.youtube_search(video_title)
        except Exception as e:
            return Response({"Error ": e})
        return Response({"results :": result})
