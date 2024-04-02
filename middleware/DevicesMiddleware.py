from fastapi import Request, HTTPException



# # Devices Middleware
# class DevicesMiddleware:
#     async def __call__(self, request: Request, call_next):
#         # Check if Devices is authenticated
#         if not self.is_devices_authenticated(request):
#             raise HTTPException(status_code=401, detail="Devices unauthorized")
#         response = await call_next(request)
#         return response

#     def is_devices_authenticated(self, request: Request):
#         # Retrieve token from header
#         token = request.headers.get("Authorization")
#         # Your authentication logic for Devices (e.g., check if the token is valid)
#         if token == "123456789":
#             return True
#         else:
#             return False


class DevicesMiddleware:
    async def __call__(self, request: Request, call_next):
        # Check Authorization header
        token = request.headers.get("Authorization")
        print("////////////////////////////////"+token)
        if token != "123456":
            raise HTTPException(status_code=401, detail="Unauthorized")
        
        # Check query parameters
        query_params = request.query_params
        # You can add logic to handle query parameters here
        
        # Check request body
        body = await request.body()
        # You can add logic to handle request body here
        
        # If everything is okay, proceed to the next handler
        response = call_next(request)
        return response