import os
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError


class Video:

    api_key = os.getenv('YOUTUBE_API_KEY')

    def __init__(self, video_id):
        self.video_id = video_id
        try:
            video = self.get_service().captions().list(videoId=video_id, part='snippet').execute()
        except HttpError as e:
            print(f'wrong video_ID, error {e.status_code}')
            self.title = None
            self.url = None
            self.view_count = None
            self.like_count = None
        else:
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
