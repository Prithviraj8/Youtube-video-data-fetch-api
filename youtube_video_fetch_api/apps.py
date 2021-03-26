# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.apps import AppConfig


class YoutubeVideoFetchApiConfig(AppConfig):
    name = 'youtube_video_fetch_api'

    def ready(self):
        from youtube_video_fetch_api.operations import scheduler
        scheduler.start()
