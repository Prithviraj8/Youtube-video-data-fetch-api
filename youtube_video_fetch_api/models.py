# Create your models here.
from django.db import models


class VideoInformation(models.Model):
    video_id = models.CharField(null=False, blank=False, max_length=200)
    video_title = models.CharField(null=True, blank=True, max_length=500)
    video_description = models.CharField(null=True, blank=True, max_length=5000)
    video_publishedDateTime = models.DateTimeField()

    @classmethod
    def create(cls, video_id, video_title, video_description, video_publishedDateTime):
        video = cls(
            video_id=video_id,
            video_title=video_title,
            video_description=video_description,
            video_publishedDateTime=video_publishedDateTime,
        )
        return video
