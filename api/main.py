from fastapi import FastAPI

from api.routers.upload_router import router as upload_router
from api.routers.candidate_router import router as candidate_router
from api.routers.search_router import router as search_router


# begin temporairement
from api.database.database import engine
from api.database.database import Base

Base.metadata.create_all(bind=engine) 
# end temporairemtn
app = FastAPI(
    title="TalentMatch AI",
    version="1.0.0",
    openapi_version="3.0.3"
)

app.include_router(upload_router)
app.include_router(candidate_router)
app.include_router(search_router)


@app.get("/")
def home():

    return {
        "message": "TalentMatch AI API"
    }