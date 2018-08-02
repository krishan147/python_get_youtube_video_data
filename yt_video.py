import requests
import pyodbc
import time
import datetime

key = "ENTER YOUR KEY HERE"

# Pull data from ACHIM SOCIAL ADDRESSBOOK.



for row_achim_social in rows_achim_social:
    yt_video_id = (row_achim_social[0])
    yt_video_published = (row_achim_social[1])
    yt_video_meta_date = (row_achim_social[2])
    yt_video_meta_data_confirm = (row_achim_social[3])
    yt_unique_id = (row_achim_social[4])
    yt_video_link = (row_achim_social[5])

    meta_data = "https://www.googleapis.com/youtube/v3/videos?id="+yt_video_id+"&part=snippet%2CcontentDetails%2Cstatistics&key=" + key
    request = requests.get(meta_data).json()
    items = request['items']

    for videos in items:

        try:
            views = videos["statistics"]["viewCount"]
        except KeyError:
            views = 0

        try:
            favourites = videos["statistics"]["favoriteCount"]
        except KeyError:
            favourites = 0

        try:
            comments = videos["statistics"]["commentCount"]
        except KeyError:
            comments = 0

        try:
            likes = videos["statistics"]["likeCount"]
        except KeyError:
            likes = 0

        try:
            dislikes = videos["statistics"]["dislikeCount"]
        except KeyError:
            dislikes = 0

        print (views,likes,dislikes,favourites,comments, yt_video_link)


        date_now = datetime.datetime.now()
        date_now_unix = time.mktime(date_now.timetuple())

        yt_video_published_unix = time.mktime(yt_video_published.timetuple())

        seven_days = 518400

        yt_video_published_unix_comparison = yt_video_published_unix + seven_days

        done = 'Y'

        if None is yt_video_meta_date:
            if date_now_unix > yt_video_published_unix_comparison:

                print (yt_video_id)

        if None is not yt_video_meta_date:
            if date_now_unix < yt_video_published_unix_comparison:
                
                print (yt_video_id)
                
            if date_now_unix > yt_video_published_unix_comparison:
                print (yt_video_id)
                
                time.sleep(15)
