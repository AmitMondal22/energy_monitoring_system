from fastapi import APIRouter, HTTPException, Response

from controllers.admin import ManageUserController, Organization,DeviceManageUserController,DeviceController

from models.organization_model import AddOrganization, EditOrganization, DeleteOrganization
from models.manage_user_model import AddUser, EditUser,DeleteUser,UserDeviceAdd,UserDeviceEdit,UserDeviceDelete


from utils.response import errorResponse, successResponse
import json

api_admin_routes = APIRouter()

# ==========================================================================
# ==========================================================================


@api_admin_routes.post("/manage_organization/add")
async def add_organization(organization:AddOrganization):
    try:
        data = Organization.add_organization(organization)   
        resdata = successResponse(data, message="User registered successfully")
        return Response(content=json.dumps(resdata), media_type="application/json", status_code=200)
    except ValueError as ve:
        # If there's a ValueError, return a 400 Bad Request with the error message
        raise HTTPException(status_code=400, detail=str(ve))
    except Exception as e:
        # For any other unexpected error, return a 500 Internal Server Error
        raise HTTPException(status_code=500, detail="Internal server error")
    
    
    
    
@api_admin_routes.get("/manage_organization/list")
async def list_organization():
    try:
        data = Organization.list_organization()
        resdata = successResponse(data, message="List of organizations")
        return Response(content=json.dumps(resdata), media_type="application/json", status_code=200)
    except ValueError as ve:
        # If there's a ValueError, return a 400 Bad Request with the error message
        raise HTTPException(status_code=400, detail=str(ve))
    except Exception as e:
        # For any other unexpected error, return a 500 Internal Server Error
        raise HTTPException(status_code=500, detail="Internal server error")
    
@api_admin_routes.post("/manage_organization/edit")
async def edit_organization(organization:EditOrganization):
    try:
        data = Organization.edit_organization(organization)
        resdata = successResponse(data, message="List of organizations")
        return Response(content=json.dumps(resdata), media_type="application/json", status_code=200)
    except ValueError as ve:
        # If there's a ValueError, return a 400 Bad Request with the error message
        raise HTTPException(status_code=400, detail=str(ve))
    except Exception as e:
        # For any other unexpected error, return a 500 Internal Server Error
        raise HTTPException(status_code=500, detail="Internal server error ")
    

@api_admin_routes.post("/manage_organization/delete")
async def delete_organization(organization:DeleteOrganization):
    try:
        data = Organization.delete_organization(organization)
        resdata = successResponse(data, message="Organization deleted successfully")
        return Response(content=json.dumps(resdata), media_type="application/json", status_code=200)
    except ValueError as ve:
        # If there's a ValueError, return a 400 Bad Request with the error message
        raise HTTPException(status_code=400, detail=str(ve))
    except Exception as e:
        # For any other unexpected error, return a 500 Internal Server Error
        raise HTTPException(status_code=500, detail="Internal server error ")



# ==========================================================================
# ==========================================================================



@api_admin_routes.post("/manage_user/add")
async def add_user(user:AddUser):
    try:
        data = ManageUserController.add_user(user)   
        resdata = successResponse(data, message="User registered successfully")
        return Response(content=json.dumps(resdata), media_type="application/json", status_code=200)
    except ValueError as ve:
        # If there's a ValueError, return a 400 Bad Request with the error message
        raise HTTPException(status_code=400, detail=str(ve))
    except Exception as e:
        # For any other unexpected error, return a 500 Internal Server Error
        raise HTTPException(status_code=500, detail="Internal server error")
    
@api_admin_routes.get("/manage_user/list")
async def list_user():
    try:
        data = ManageUserController.list_user()
        resdata = successResponse(data, message="List of users")
        return Response(content=json.dumps(resdata), media_type="application/json", status_code=200)
    except ValueError as ve:
        # If there's a ValueError, return a 400 Bad Request with the error message
        raise HTTPException(status_code=400, detail=str(ve))
    except Exception as e:
        # For any other unexpected error, return a 500 Internal Server Error
        raise HTTPException(status_code=500, detail="Internal server error")
    
@api_admin_routes.get("/manage_user/list/{user_id}")
async def list_user(user_id:int):
    try:
        data = ManageUserController.user_info(user_id)
        resdata = successResponse(data, message="List of users")
        return Response(content=json.dumps(resdata), media_type="application/json", status_code=200)
    except ValueError as ve:
        # If there's a ValueError, return a 400 Bad Request with the error message
        raise HTTPException(status_code=400, detail=str(ve))
    except Exception as e:
        # For any other unexpected error, return a 500 Internal Server Error
        raise HTTPException(status_code=500, detail="Internal server error")
    
@api_admin_routes.post("/manage_user/edit")
async def edit_user(user:EditUser):
    try:
        data = ManageUserController.edit_user(user)
        resdata = successResponse(data, message="List of users")
        return Response(content=json.dumps(resdata), media_type="application/json", status_code=200)
    except ValueError as ve:
        # If there's a ValueError, return a 400 Bad Request with the error message
        raise HTTPException(status_code=400, detail=str(ve))
    except Exception as e:
        # For any other unexpected error, return a 500 Internal Server Error
        raise HTTPException(status_code=500, detail="Internal server error ")


@api_admin_routes.post("/manage_user/delete")
async def delete_user(user:DeleteUser):
    try:
        data = ManageUserController.delete_user(user)
        resdata = successResponse(data, message="User deleted successfully")
        return Response(content=json.dumps(resdata), media_type="application/json", status_code=200)
    except ValueError as ve:
        # If there's a ValueError, return a 400 Bad Request with the error message
        raise HTTPException(status_code=400, detail=str(ve))
    except Exception as e:
        # For any other unexpected error, return a 500 Internal Server Error
        raise HTTPException(status_code=500, detail="Internal server error ")
    
# =================================================================================================
# =================================================================================================



@api_admin_routes.post("/manage_user/add_device")
async def add_device(user:UserDeviceAdd):
    try:
        data = DeviceManageUserController.add_device(user)
        resdata = successResponse(data, message="Device added successfully")
        return Response(content=json.dumps(resdata), media_type="application/json", status_code=200)
    except ValueError as ve:
        # If there's a ValueError, return a 400 Bad Request with the error message
        raise HTTPException(status_code=400, detail=str(ve))
    except Exception as e:
        # For any other unexpected error, return a 500 Internal Server Error
        raise HTTPException(status_code=500, detail="Internal server error")
    
@api_admin_routes.get("/manage_user/list_user_device")
async def list_user_device():
    try:
        data = DeviceManageUserController.list_user_device()
        resdata = successResponse(data, message="List of users")
        return Response(content=json.dumps(resdata), media_type="application/json", status_code=200)
    except ValueError as ve:
        # If there's a ValueError, return a 400 Bad Request with the error message
        raise HTTPException(status_code=400, detail=str(ve))
    except Exception as e:
        # For any other unexpected error, return a 500 Internal Server Error
        raise HTTPException(status_code=500, detail="Internal server error")
    
    
@api_admin_routes.post("/manage_user/edit_user_device")
async def edit_user_device(user:UserDeviceEdit):
    try:
        data = DeviceManageUserController.edit_device(user)
        resdata = successResponse(data, message="List of users")
        return Response(content=json.dumps(resdata), media_type="application/json", status_code=200)
    except ValueError as ve:
        # If there's a ValueError, return a 400 Bad Request with the error message
        raise HTTPException(status_code=400, detail=str(ve))
    except Exception as e:
        # For any other unexpected error, return a 500 Internal Server Error
        raise HTTPException(status_code=500, detail="Internal server error ")
    
    
@api_admin_routes.post("/manage_user/delete_user_device")
async def delete_user_device(user:UserDeviceDelete):
    try:
        data = DeviceManageUserController.delete_device(user)
        resdata = successResponse(data, message="List of users")
        return Response(content=json.dumps(resdata), media_type="application/json", status_code=200)
    except ValueError as ve:
        # If there's a ValueError, return a 400 Bad Request with the error message
        raise HTTPException(status_code=400, detail=str(ve))
    except Exception as e:
        # For any other unexpected error, return a 500 Internal Server Error
        raise HTTPException(status_code=500, detail="Internal server error ")
    
# =================================================================================================
# =================================================================================================

@api_admin_routes.get("/devices/list")
async def list_device():
    try:
        data = await DeviceController.list_device()
        resdata = successResponse(data, message="List of devices")
        return Response(content=json.dumps(resdata), media_type="application/json", status_code=200)
    except ValueError as ve:
        # If there's a ValueError, return a 400 Bad Request with the error message
        raise HTTPException(status_code=400, detail=str(ve))
    except Exception as e:
        # For any other unexpected error, return a 500 Internal Server Error
        raise HTTPException(status_code=500, detail="Internal server error")