from pymongo import MongoClient

from repository.musicStorage.music_storage import MusicStorageRepository
from model.music.playlist import Playlist

class MusicStorageRepositoryImpl(MusicStorageRepository):
    def __init__(self, cli:MongoClient):
        self.cli = cli
        
    def get_playlist_by_user_id(self, userID: str)-> Playlist:
        return Playlist()

def NewMusicStorageRepository(cli: MongoClient)-> MusicStorageRepository:
    return MusicStorageRepositoryImpl(
        cli=cli
    )