from fastapi import FastAPI, APIRouter

from views import user_router, assets_router
from views_sync import sync_router


app = FastAPI()
router = APIRouter()

@router.get('/')
def first():
    return 'Hello world!'

app.include_router(prefix='/first', router=router)
app.include_router(user_router)
app.include_router(assets_router)
app.include_router(sync_router)
