import os
from googleapiclient.discovery import build
import json

class Channel:

    """Класс для ютуб-канала"""

    api_key = os.getenv('YOUTUBE_API_KEY')
    youtube = build('youtube', 'v3', developerKey=api_key)

    # Функция build из googleapiclient.discovery позволяет создать ресурс для обращения к API,
    # то есть это некая абстракция над REST API Drive, чтобы удобнее обращаться к методам API.


    def __init__(self, channel_id, title, description, url, subscriberCount, videoCount, viewCount) -> None:

        self.channel_id = channel_id
        self.title = title
        self.description = description
        self.url = url
        self.subscriberCount = subscriberCount
        self.videoCount = videoCount
        self.viewCount = viewCount


    @classmethod
    def get_service(cls, channel_id):
        """
        Метод возвращает объект для работы с YouTube API
        """
        # api_key = os.getenv('YOUTUBE_API_KEY')
        # youtube = build('youtube', 'v3', developerKey=api_key)
        channel = cls.youtube.channels().list(id=channel_id, part='snippet,statistics').execute()

        return channel


    def to_json(self):
        """
        Метод сохраняет в файл значения атрибутов экземпляра
        """
        channel = self.youtube.channels().list(id=self.channel_id, part='snippet,statistics').execute()
        channel_json = json.dumps(channel, indent=2, ensure_ascii=False)

        return channel_json
