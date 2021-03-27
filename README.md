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
    * Inside the setting.py file, fill the variable DEVELOPER_KEYS with all the API Keys available,the list should be filled as ['API_KEY_1', 'API_KEY_2',...]

## The project handles if any api key is invalid, or runs out of quota.

![Screenshot 2021-03-27 at 1 37 28 PM](https://user-images.githubusercontent.com/31995793/112714699-94da3600-8f01-11eb-8494-02c406b1956c.png)

## Results(videos list) appear in a chronological order of their published date & time
![Screenshot 2021-03-27 at 1 37 40 PM](https://user-images.githubusercontent.com/31995793/112714706-9ad01700-8f01-11eb-96a9-789845aba6bc.png)

 
## Code formatting

I have used the [black](https://black.readthedocs.io/en/stable/) to format this project.

You can [integrate black with your IDE](https://black.readthedocs.io/en/stable/editor_integration.html) to format on save. You may also add a pre-commit hook. To add the hook, run `pre-commit install` (after installing the dependencies from `requirements.txt`).

To simply use the default settings of black and try the code formatter, run the command:
```
black .
```
in a directory and see the magic.
