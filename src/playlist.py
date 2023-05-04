import os
from googleapiclient.discovery import build
import pprint
from datetime import timedelta
import isodate


class PlayList:
    api_key = os.getenv('YOUTUBE_API_KEY')

    def __init__(self, playlist_id):
        self.playlist_id = playlist_id
        playlist = self.get_service().playlists().list(id=playlist_id, part='snippet, contentDetails').execute()
        self.title = playlist['items'][0]['snippet']['title']
        self.url = 'https://www.youtube.com/playlist?list=' + self.playlist_id

    @classmethod
    def get_service(cls):
        youtube = build('youtube', 'v3', developerKey=cls.api_key)

        return youtube

    def get_id(self):
        '''id видеороликов из плейлиста'''

        playlist_videos = self.get_service().playlistItems().list(playlistId=self.playlist_id,
                                                       part='contentDetails',
                                                       maxResults=50,
                                                       ).execute()
        video_ids: list[str] = [video['contentDetails']['videoId'] for video in playlist_videos['items']]

        return video_ids

    def get_video_response(self):
        '''получает информацию о видео'''

        video_response = self.get_service().videos().list(part='contentDetails,statistics',
                                                          id=','.join(self.get_id())
                                                          ).execute()

        return video_response


    @property
    def total_duration(self):
        '''возвращает объект класса `datetime.timedelta` с суммарной длительность плейлиста'''

        total_duration = timedelta()
        for video in self.get_video_response()['items']:
            iso_8601_duration = video['contentDetails']['duration']
            duration = isodate.parse_duration(iso_8601_duration)
            list_time = duration.__str__().split(':')
            duration = timedelta(hours=int(list_time[0]), minutes=int(list_time[1]), seconds=int(list_time[2]))
            total_duration += duration

        return total_duration

    def show_best_video(self):
        '''возвращает ссылку на самое популярное видео из плейлиста (по количеству лайков)'''

        likes = 0

        for video in self.get_video_response()['items']:
            if int(video['statistics']['likeCount']) > likes:
                likes = int(video['statistics']['likeCount'])
                best_video = "https://youtu.be/" + video['id']

        return best_video
