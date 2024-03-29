from fastapi.responses import JSONResponse, StreamingResponse,Response
from fastapi import Request,Header,HTTPException
from typing import Coroutine, Any,Callable,Awaitable
from fastapi.encoders import jsonable_encoder

from fastapi import FastAPI
 
my_middleware_app = FastAPI()
 
@my_middleware_app.middleware("http")
async def my_func(request: Request, call_next):
    if "Authorization" in request.headers:
        print(request.headers["Authorization"])
 
        request.state.name = "amit"
        response = await call_next(request)
        return response
    else:
        return JSONResponse(content=jsonable_encoder("Authorization header not provided."))
    
    
    

# async def auth_required_middleware(request: Request, call_next: Coroutine):
#     """Middleware for authenticating users on required routes"""
#     token = str(
#         request.cookies.get("token")
#     )  # Stringyfy-ing because pyjwt might cry if it gets NoneType

#     try:
#         user_id = JWTService.verify_and_return_id(token)
#         request.state.user_id = user_id
#         response: StreamingResponse = await call_next(request)
#         return response
#     except:
#         return JSONResponse(content={"description": "Unauthorized"}, status_code=401)


# async def public_required_middleware(request: Request, call_next: Coroutine):
#     """Middleware for authenticating users on required routes"""
#     # token = str(
#     #     request.cookies.get("token")
#     # )  # Stringyfy-ing because pyjwt might cry if it gets NoneType

#     try:
#         user_id = 1
#         request.user_id = user_id
#         response: StreamingResponse = await call_next(request)
#         return response
#     except:
#         return JSONResponse(content={"description": "Unauthorized"}, status_code=401)



# async def public_required_middleware(request: Request, call_next, authorization: str = Header(None)):
#     """Middleware for authenticating users on required routes"""
#     try:
#         if authorization == "Bearer token":  # Replace "Bearer token" with your expected header value
#             user_id = 1  # Placeholder for authentication logic
#             request.state.user_id = user_id
#             response = await call_next(request)
#             return response
#         else:
#             raise HTTPException(status_code=401, detail="Unauthorized")
#     except HTTPException as http_exception:
#         raise http_exception
#     except Exception as e:
#         raise HTTPException(status_code=500, detail="Internal Server Error")




# async def public_required_middleware(request: Request, call_next: Any,authorization: str = Header(None)):
#     """Middleware for authenticating users on required routes"""
#     try:
#         user_id = 1  # Example user ID, replace with your actual authentication logic
#         request.state.user_id = user_id
#         response = await call_next(request)
#         return response
#     except:
#         return JSONResponse(content={"description": "Unauthorized"}, status_code=401)

