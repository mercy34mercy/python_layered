from pydantic import BaseModel
from fastapi import Depends

from usecase.get_playlist_by_user_id import GetPlaylistByUserID, NewGetPlaylistByUserID

class GetPlaylistHandlerInput(BaseModel):
    user_id: int

class GetPlaylistHandlerOutput(BaseModel):
    name: str
    description: str
    public: bool
    user_id: int
    created_at: str
    updated_at: str


def getPlaylistByUserIDHandler(input: GetPlaylistHandlerInput,usecase: GetPlaylistByUserID = Depends(NewGetPlaylistByUserID)):
    return usecase.execute(input.user_id)