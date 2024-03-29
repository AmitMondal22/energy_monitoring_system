from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
import uvicorn

from db_model.MASTER_MODEL import select_data
from datetime import datetime, date
from routes import user_routes,auth_routes,public_routes






app = FastAPI()

# Set up CORS
origins = [
    "http://localhost",
    "http://localhost:8080",
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
app.include_router(public_routes.public_routes, prefix="/api/device", tags=["public_device"])

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
    uvicorn.run("main:app", host="0.0.0.0", port=8080, reload=True)
    
    
# if __name__ == "__main__":
#     try:
#         uvicorn.run(app, host="0.0.0.0", port=8000)
#     except KeyboardInterrupt:
#         print("KeyboardInterrupt: Stopping the server...")
