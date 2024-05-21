import unittest
from typing import Dict

from model.music.playlist import Playlist
from repository.musicStorage.music_storage import MusicStorageRepository
from usecase.get_playlist_by_user_id import GetPlaylistByUserID



class MusicStorageRepositoryMock(MusicStorageRepository):
    def __init__(
            self, 
            playlists: Dict[str, Playlist],
            exception: Exception = None
        ):
        self.playlists = playlists
        self.exception = exception

    def get_playlist_by_user_id(self, userID: str) -> Playlist:
        if self.exception is not None:
            raise self.exception
        return self.playlists[userID]


class TestGetPlaylistByUserID(unittest.TestCase):
    def test_execute(self):
        cases = [
            {
                "name": "success",
                "input": {
                    "context": "context",
                    "queue_id": "queue_id"
                },
                "expected": {
                    "result": "result",
                    "exception": None
                }
            },
            {
                "name": "error",
                "input": {
                    "context": "context",
                    "queue_id": "queue_id"
                },
                "expected": {
                    "result": None,
                    "exception": "exception"
                }
            }
        ]

        for c in cases:
            music_storage_repo = MusicStorageRepositoryMock(c["expected"]["result"], c["expected"]["exception"])
            get_playlist_by_user_id = GetPlaylistByUserID(music_storage_repo)

            result, exception = get_playlist_by_user_id.execute(c["input"]["context"], c["input"]["queue_id"])

            self.assertEqual(result, c["expected"]["result"])
            self.assertEqual(exception, c["expected"]["exception"])

if __name__ == "__main__":
    unittest.main()