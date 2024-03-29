from fastapi import APIRouter, HTTPException, Response
from controllers.auth import AuthController
from models import auth_model
from utils_package.response import errorResponse, successResponse
import json

auth_routes = APIRouter()


@auth_routes.post("/register")
async def register(user: auth_model.Register):
    try:
        data = await AuthController.register(user)   
        resdata = successResponse(data, message="User registered successfully")
        return Response(content=json.dumps(resdata), media_type="application/json", status_code=200)
    except ValueError as ve:
        # If there's a ValueError, return a 400 Bad Request with the error message
        raise HTTPException(status_code=400, detail=str(ve))
    except Exception as e:
        # For any other unexpected error, return a 500 Internal Server Error
        raise HTTPException(status_code=500, detail="Internal server error")
    
    
@auth_routes.post("/login")
async def login(user: auth_model.Login):
    try:
        data = await AuthController.login(user)
        resdata = successResponse(data, message="User logged in successfully")
        return Response(content=json.dumps(resdata), media_type="application/json", status_code=200)
    except ValueError as ve:
        # If there's a ValueError, return a 400 Bad Request with the error message
        raise HTTPException(status_code=400, detail=str(ve))
    except Exception as e:
        # For any other unexpected error, return a 500 Internal Server Error
        raise HTTPException(status_code=500, detail="Internal server error")