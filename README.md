# Youtube video data fetch api

## An API to fetch videos from youtube in chronological order of their publishing date-time for a given tag/search query.

## Steps to run the api:
  * Clone the repository in a directory on your computer
  * Open terminal and cd into the outer <b>Youtube-Videos-Fetch-Api</b> directory
  * Install all dependencies by using typing `pip install -r requirements.txt` in the terminal
  * Run, `python manage.py runserver --noreload` in the terminal
  * Open postman, and type `http://127.0.0.1:8000/youtube_video_fetch?video_title=superman` in the <b>Enter request URL</b> tab
    * Note: video_title is a query parameter and you can give it any value(eg: superman) to get the seach results based on that, from youtube.
    * Also, the search results will be stored in the database, every 0.1 minute, as long as the server is running.
 
