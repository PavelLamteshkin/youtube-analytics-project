import os
from googleapiclient.discovery import build
import json


class Channel:

    """Класс для ютуб-канала"""

    api_key = os.getenv('YOUTUBE_API_KEY')


    def __init__(self, channel_id) -> None:

        self.channel_id = channel_id


    @classmethod
    def get_service(cls):
        """
        Метод возвращает объект для работы с YouTube API
        """

        youtube = build('youtube', 'v3', developerKey=cls.api_key)

        return youtube


    @classmethod
    def to_json(cls, channel_id):
        """
        Метод сохраняет в файл значения атрибутов экземпляра
        """
        channel = cls.get_service().channels().list(id=channel_id, part='snippet,statistics').execute()

        cls.title = channel['items'][0]['snippet']['title']
        cls.description = channel['items'][0]['snippet']['description']
        cls.url = channel['items'][0]['snippet']['thumbnails']['default']['url']
        cls.subscriberCount = channel['items'][0]['statistics']['subscriberCount']
        cls.videoCount = channel['items'][0]['statistics']['videoCount']
        cls.viewCount = channel['items'][0]['statistics']['viewCount']

        return channel


    def print_info(self, channel):

        return json.dumps(channel, indent=2, ensure_ascii=False)
