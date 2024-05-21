from fastapi import FastAPI, APIRouter
import pymongo

from handler.health.health import healthHandler
from handler.v1.get_playlist_by_user_id import getPlaylistByUserIDHandler, GetPlaylistHandlerInput, GetPlaylistHandlerOutput
from usecase.get_playlist_by_user_id import NewGetPlaylistByUserID
from repository.musicStorage.mongodb.mongodb import NewMusicStorageRepository, MusicStorageRepository

def newMongoDBClient()-> pymongo.MongoClient:
    client = pymongo.MongoClient("localhost", 27017)
    return client

v1Router = APIRouter(
    prefix="/v1",
    tags=["v1"],
    responses={404: {"description": "Not found"}},
)

healthRouter = APIRouter(
    prefix="/health",
    tags=["health"],
    responses={404: {"description": "Not found"}},
)

# init musicstorage repository
musicStorageRepo:MusicStorageRepository = NewMusicStorageRepository(newMongoDBClient())

# ヘルスチェック用
@healthRouter.get("/")
async def health():
    return healthHandler()

@v1Router.post("/getPlaylistByUserID")
async def getPlaylistByUserID(getPlaylistHandlerInput: GetPlaylistHandlerInput)->GetPlaylistHandlerOutput:
    return getPlaylistByUserIDHandler(input=getPlaylistHandlerInput, usecase=NewGetPlaylistByUserID(musicStorageRepo))

app = FastAPI()
app.include_router(v1Router)
app.include_router(healthRouter)