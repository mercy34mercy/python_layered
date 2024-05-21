from fastapi import Depends

from abc import ABC, abstractmethod
from typing import Any, Tuple

from model.music.playlist import Playlist
from repository.musicStorage.music_storage import MusicStorageRepository

class GetPlaylistByUserID(ABC):
    @abstractmethod
    def execute(self, context: Any, queue_id: Any) -> Tuple[Any, Exception]:
        pass

class GetPlaylistByUserIDImpl(GetPlaylistByUserID):

    def __init__(self, music_storage_repo: MusicStorageRepository):
        self.music_storage_repo = music_storage_repo

    def execute(self, context: Any, queue_id: Any) -> Tuple[Playlist, Exception]:
        try:
            result = self.music_storage_repo.get_playlist_by_user_id(context, queue_id)
            return result, None
        except Exception as e:
            return None, e

def NewGetPlaylistByUserID(music_storage_repo: MusicStorageRepository = Depends(MusicStorageRepository)) -> GetPlaylistByUserID:
    return GetPlaylistByUserIDImpl(music_storage_repo)