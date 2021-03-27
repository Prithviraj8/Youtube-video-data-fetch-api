import json
from datetime import datetime, timedelta
from pprint import pprint

import apiclient
from googleapiclient.discovery import build
from youtube_video_fetch_api.models import VideoInformation
from youtube_video_fetch import settings

DEVELOPER_KEYS = settings.DEVELOPER_KEYS
YOUTUBE_API_SERVICE_NAME = settings.YOUTUBE_API_SERVICE_NAME
YOUTUBE_API_VERSION = settings.YOUTUBE_API_VERSION

"""
Using *cricket* as default to search for results from youtube data api
"""


def youtube_search(
    q="cricket",
    max_results=50,
    order="relevance",
    token=None,
    location=None,
    location_radius=None,
):
    search_response = {}
    for developerKey in DEVELOPER_KEYS:
        try:
            youtube = build(
                YOUTUBE_API_SERVICE_NAME, YOUTUBE_API_VERSION, developerKey=developerKey
            )
            time_now = datetime.now()
            last_request_time = time_now - timedelta(minutes=5)
            search_response = (
                youtube.search()
                .list(
                    q=q,
                    type="video",
                    pageToken=token,
                    order=order,
                    part="id,snippet",
                    maxResults=max_results,
                    location=location,
                    locationRadius=location_radius,
                    publishedAfter=(last_request_time.replace(microsecond=0).isoformat() + "Z"),
                )
                .execute()
            )
            valid_key = True
        except apiclient.errors.HttpError as err:
            # Sending an appropriate error message when google api provided is invalid
            err = json.loads(err.content)['error']['message']
            return err

        if valid_key:
            break

    videos = []

    for search_result in search_response.get("items", []):
        if search_result["id"]["kind"] == "youtube#video":
            video_info = {
                "video_id": search_result["id"]["videoId"],
                "video_title": search_result["snippet"]["title"],
                "video_description": search_result["snippet"]["description"],
                "video_publishedDateTime": search_result["snippet"]["publishedAt"],
            }
            videos.append(video_info)
            save_video_information(**video_info)

    try:
        next_token = search_response["nextPageToken"]
        return next_token, videos
    except Exception as e:
        nexttok = "last_page"
        return nexttok, videos


"""
Saving fetched videos information to local database in save_video_information() funcition.
"""


def save_video_information(
    video_id, video_title, video_description, video_publishedDateTime
):
    print("SAVING", video_id, video_title, video_description, video_publishedDateTime)
    video = VideoInformation().create(
        video_id=str(video_id),
        video_title=str(video_title),
        video_description=str(video_description),
        video_publishedDateTime=video_publishedDateTime,
    )
    video.save()
