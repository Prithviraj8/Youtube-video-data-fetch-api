from apscheduler.schedulers.background import BackgroundScheduler
from . import youtube_videos


def start():
    scheduler = BackgroundScheduler()
    scheduler.add_job(youtube_videos.youtube_search, 'interval', minutes=0.1)
    scheduler.start()
