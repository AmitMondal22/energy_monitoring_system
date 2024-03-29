from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
import uvicorn

from db_model.MASTER_MODEL import select_data
from datetime import datetime, date
from routes import devices_routes, user_routes,auth_routes





app = FastAPI()


# Set up CORS
origins = [
    "http://192.168.29.210:8000",
    "http://localhost:8000"
]

# @app.middleware("http")

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)



# Include user routes
app.include_router(auth_routes.auth_routes, prefix="/api/auth", tags=["auth"])

# Include user routes
app.include_router(user_routes.user_rutes, prefix="/api/user", tags=["user"])

# Include user routes
app.include_router(devices_routes.devices_routes, prefix="/api/device", tags=["device"])

# Index route
@app.get('/')
def index():
    return "hello fastapi index"  # Corrected typo

# Users route
@app.get('/users')
async def users():
    try:
        data = select_data()
        return data
    except Exception as e:
        print(e)
        raise HTTPException(status_code=500, detail="Internal server error")
    


if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)
    