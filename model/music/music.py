from pydantic import BaseModel

class Music(BaseModel):
    title: str
    artist: str
    album: str
    year: int