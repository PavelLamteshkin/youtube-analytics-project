import os
from googleapiclient.discovery import build


class Video:

    api_key = os.getenv('YOUTUBE_API_KEY')

    def __init__(self, video_id):
        self.video_id = video_id
        video = self.get_service().videos().list(id=video_id, part='snippet,statistics').execute()
        self.title = video['items'][0]['snippet']['title']
        self.url = 'https://www.youtube.com/watch?v=' + self.video_id
        self.view_count = video['items'][0]['statistics']['viewCount']
        self.like_count = video['items'][0]['statistics']['likeCount']


    @classmethod
    def get_service(cls):
        """
        Метод возвращает объект для работы с YouTube API
        """

        youtube = build('youtube', 'v3', developerKey=cls.api_key)

        return youtube

    def __str__(self):
        return f'{self.title}'


class PLVideo(Video):

    def __init__(self, video_id, list_id):
        super().__init__(video_id)
        self.list_id = list_id


# api_key = os.getenv('YOUTUBE_API_KEY')
# channel_id = 'UC1eFXmJNkjITxPFWTy6RsWg'
# youtube = build('youtube', 'v3', developerKey=api_key)
# channel = youtube.channels().list(id=channel_id, part='snippet,statistics').execute()
# print(channel)

# video1 = Video('9lO06Zxhu88')
# api_key = os.getenv('YOUTUBE_API_KEY')
# youtube = build('youtube', 'v3', developerKey=api_key)
# channel = youtube.videos().list(id='9lO06Zxhu88', part='snippet,statistics').execute()
# print(channel)

# video1 = Video('BBotskuyw_M')
# print(video1.url)