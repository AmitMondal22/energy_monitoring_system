from fastapi import APIRouter, HTTPException, Response, Depends, Request
from utils_package.response import errorResponse, successResponse
import json

from middleware.MyMiddleware import public_required_middleware

public_routes = APIRouter()


# public_routes.middleware("http")(
#     public_required_middleware
# )

# # public_routes.get("/abc", tags=["public"], dependencies=[Depends(route_authentication_middleware)])
# @public_routes.get("/abc", dependencies=[Depends(public_required_middleware)])
# async def get_abc(request: Request):
#     try:
#         user_id = request.user_id
#         return {"user_id": user_id}
#     except:
#         return "error"
    
# @public_routes.get("/abc", dependencies=[Depends(public_required_middleware)])
# async def get_abc(request: Request):
#     # try:
#         user_id = request.state.user_id
#         return {"user_id": user_id}
#     # except:
#     #     return "error"


@public_routes.get("/abc", dependencies=[Depends(public_required_middleware)])
async def get_abc(request: Request):
    # try:
        user_id = request.state.user_id
        return {"user_id": user_id}
    # except:
    #     raise HTTPException(status_code=500, detail="Internal Server Error")
