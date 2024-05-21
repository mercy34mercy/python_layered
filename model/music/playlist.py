from pydantic import BaseModel

class Playlist(BaseModel):
    name: str
    description: str
    public: bool
    user_id: int
    created_at: str
    updated_at: str