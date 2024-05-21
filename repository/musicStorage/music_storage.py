from abc import ABC, abstractmethod
from model.music.playlist import Playlist

class MusicStorageRepository(ABC):
    @abstractmethod
    def get_playlist_by_user_id(self, userID: str) -> Playlist:
        pass
