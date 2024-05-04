from fastapi import APIRouter, HTTPException, Response,WebSocket,WebSocketDisconnect

from controllers.admin import ClientController, ManageUserController, DeviceManageUserController,DeviceController

from controllers.unit import UnitController
from controllers.alert import AlertController

from models.organization_model import AddOrganization, EditOrganization, DeleteOrganization,ListOrganization
from models.manage_user_model import AddUser, EditUser,DeleteUser,UserDeviceAdd,UserDeviceEdit,UserDeviceDelete,ListUsers,UserInfo,ClientId,DeviceInfo



from models.device_data_model import EnergyData,AddAlert,DeviceAdd,DeviceEdit,EditAlert,DeleteAlert,EnergyUsed
from Library.DecimalEncoder import DecimalEncoder
from Library.CustomEncoder import CustomEncoder
from db_model.MASTER_MODEL import select_one_data



from Library import EmailLibrary

from Library.WsConnectionManager import WsConnectionManager
from utils.response import errorResponse, successResponse

from typing import List
import json

api_client_routes = APIRouter()
manager = WsConnectionManager()

# ==========================================================================
# ==========================================================================

# both
@api_client_routes.websocket("/ws")
async def websocket_endpoint(websocket: WebSocket):
    await manager.connect(websocket)
    try:
        while True:
            data = await websocket.receive_text()
            await manager.send_personal_message(f"Received:{data}",websocket)
    except WebSocketDisconnect:
        manager.disconnect(websocket)
        await manager.send_personal_message("Bye!!!",websocket)
        
#  send_message      
@api_client_routes.get("/send_message")
async def send_message(message: str):
    await manager.broadcast(message)
    return {"message": "Sent message: {}".format(message)}

# daynamic data
@api_client_routes.websocket("/ws/{user_id}")
async def websocket_endpoint(websocket: WebSocket, user_id: int):
    await manager.connect(user_id, websocket)
    try:
        while True:
            data = await websocket.receive_text()
            await manager.send_personal_message(user_id, f"Message '{data}' received from user {user_id}")
    except Exception as e:
        manager.disconnect(user_id)
        print(f"Connection with user {user_id} closed.")
        
# @api_client_routes.post("/send_message/{user_id}")
# async def send_message(user_id: int, message: str):
#     await manager.send_personal_message(user_id, message)
#     return {"message": "Message sent successfully"}


@api_client_routes.post("/send_message/{client_id}/{device_id}/{device}/{message}")
async def send_message(client_id: int,device_id:int,device:str, message: str):
    await manager.send_personal_message(client_id, device_id, device, json.dumps(message))
    return {"message": "Message sent successfully"}


@api_client_routes.websocket("/ws/{client_id}/{device_id}/{device}")
async def websocket_endpoint(websocket: WebSocket, client_id: str, device_id: str, device: str):
    await manager.connect(client_id, device_id, device, websocket)
    try:
        while True:
            data = await websocket.receive_text()
            await manager.send_personal_message(client_id, device_id, device, f"Message '{data}' received from user {client_id}-{device_id}-{device}")
    except Exception as e:
        manager.disconnect(websocket,client_id, device_id, device)
        print(f"Connection with user {client_id}-{device_id}-{device} closed.")


# ================================================================
# ================================================================
class SendEnergySocket:
    @staticmethod
    async def send_last_energy_data(client_id, device_id, device):
        try:
            # Lazy import inside the function
            # from Library import WsConnectionManager
            # manager = WsConnectionManager.WsConnectionManager()
            
            select="energy_data_id, client_id, device_id, e1, e2, e3, r, y, b, r_y, y_b, b_y, curr1, curr2, curr3, activep1, activep2, activep3, apparentp1, apparentp2, apparentp3, pf1, pf2, pf3, freq, reactvp1, reactvp2, reactvp3, avaragevln, avaragevll, avaragecurrent, totkw, totkva, totkvar, runhr, date, time, DATE_FORMAT(created_at, '%Y-%m-%d %H:%i:%s') AS created_at"
            condition = f"device_id = '{device_id}' AND device ='{device}' AND client_id = '{client_id}'"
            order_by="energy_data_id DESC"
                
            lastdata = select_one_data("td_energy_data", select, condition, order_by)
           
            await manager.send_personal_message(client_id, device_id, device, json.dumps(lastdata, cls=DecimalEncoder))
            
            # await manager.send_personal_message(client_id, device_id, device, json.dumps("hello134"))
            
            
            # await manager.send_personal_message(1, 1, "aa", json.dumps("hello world"))
            print("lastdata last energy data>>>>>>>>>>/////////",lastdata)
            return lastdata
        except Exception as e:
            raise ValueError("Could not fetch data")
# ================================================================
# ================================================================
    
# ==========================================================================
# ==========================================================================


@api_client_routes.post("/manage_organization/add")
async def add_organization(organization:AddOrganization):
    try:
        data = ClientController.add_organization(organization)   
        resdata = successResponse(data, message="User registered successfully")
        return Response(content=json.dumps(resdata), media_type="application/json", status_code=200)
    except ValueError as ve:
        # If there's a ValueError, return a 400 Bad Request with the error message
        raise HTTPException(status_code=400, detail=str(ve))
    except Exception as e:
        # For any other unexpected error, return a 500 Internal Server Error
        raise HTTPException(status_code=500, detail="Internal server error")
    
    
    
    
@api_client_routes.post("/manage_organization/list")
async def list_organization(params:ListOrganization):
    try:
        # print(params)
        data = ClientController.list_organization(params)
        resdata = successResponse(data, message="List of organizations")
        return Response(content=json.dumps(resdata), media_type="application/json", status_code=200)
    except ValueError as ve:
        # If there's a ValueError, return a 400 Bad Request with the error message
        raise HTTPException(status_code=400, detail=str(ve))
    except Exception as e:
        # For any other unexpected error, return a 500 Internal Server Error
        raise HTTPException(status_code=500, detail="Internal server error")
    
@api_client_routes.post("/manage_organization/edit")
async def edit_organization(organization:EditOrganization):
    try:
        data = ClientController.edit_organization(organization)
        resdata = successResponse(data, message="List of organizations")
        return Response(content=json.dumps(resdata), media_type="application/json", status_code=200)
    except ValueError as ve:
        # If there's a ValueError, return a 400 Bad Request with the error message
        raise HTTPException(status_code=400, detail=str(ve))
    except Exception as e:
        # For any other unexpected error, return a 500 Internal Server Error
        raise HTTPException(status_code=500, detail="Internal server error ")
    

@api_client_routes.post("/manage_organization/delete")
async def delete_organization(organization:DeleteOrganization):
    try:
        data = ClientController.delete_organization(organization)
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



@api_client_routes.post("/manage_user/add")
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
    
@api_client_routes.post("/manage_user/list")
async def list_user(params:ListUsers):
    try:
        data = ManageUserController.list_user(params)
        resdata = successResponse(data, message="List of users")
        return Response(content=json.dumps(resdata), media_type="application/json", status_code=200)
    except ValueError as ve:
        # If there's a ValueError, return a 400 Bad Request with the error message
        raise HTTPException(status_code=400, detail=str(ve))
    except Exception as e:
        # For any other unexpected error, return a 500 Internal Server Error
        raise HTTPException(status_code=500, detail="Internal server error")
    
@api_client_routes.post("/manage_user/list_user")
# @api_client_routes.get("/manage_user/list_user/{user_id}")
async def list_user(params:UserInfo):
    try:
        data = ManageUserController.user_info(params)
        resdata = successResponse(data, message="List of users")
        return Response(content=json.dumps(resdata), media_type="application/json", status_code=200)
    except ValueError as ve:
        # If there's a ValueError, return a 400 Bad Request with the error message
        raise HTTPException(status_code=400, detail=str(ve))
    except Exception as e:
        # For any other unexpected error, return a 500 Internal Server Error
        raise HTTPException(status_code=500, detail="Internal server error")
    
@api_client_routes.post("/manage_user/edit")
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


@api_client_routes.post("/manage_user/delete")
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



@api_client_routes.post("/manage_user/add_device")
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
    
@api_client_routes.post("/manage_user/list_user_device")
async def list_user_device(params:ClientId):
    try:
        data = DeviceManageUserController.list_user_device(params)
        resdata = successResponse(data, message="List of users")
        return Response(content=json.dumps(resdata), media_type="application/json", status_code=200)
    except ValueError as ve:
        # If there's a ValueError, return a 400 Bad Request with the error message
        raise HTTPException(status_code=400, detail=str(ve))
    except Exception as e:
        # For any other unexpected error, return a 500 Internal Server Error
        raise HTTPException(status_code=500, detail="Internal server error")
    
    
@api_client_routes.post("/manage_user/edit_user_device")
async def edit_user_device(user:UserDeviceEdit):
    try:
        data = DeviceManageUserController.edit_device(user)
        resdata = successResponse(data, message="List of user devices")
        return Response(content=json.dumps(resdata), media_type="application/json", status_code=200)
    except ValueError as ve:
        # If there's a ValueError, return a 400 Bad Request with the error message
        raise HTTPException(status_code=400, detail=str(ve))
    except Exception as e:
        # For any other unexpected error, return a 500 Internal Server Error
        raise HTTPException(status_code=500, detail="Internal server error ")
    
    
@api_client_routes.post("/manage_user/delete_user_device")
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

@api_client_routes.post("/devices/list")
async def list_device(params:ClientId):
    try:
        data = await DeviceController.list_device(params)
        resdata = successResponse(data, message="List of devices")
        return Response(content=json.dumps(resdata), media_type="application/json", status_code=200)
    except ValueError as ve:
        # If there's a ValueError, return a 400 Bad Request with the error message
        raise HTTPException(status_code=400, detail=str(ve))
    except Exception as e:
        # For any other unexpected error, return a 500 Internal Server Error
        raise HTTPException(status_code=500, detail="Internal server error")
    
    
    
@api_client_routes.post("/devices/device_info")
async def list_device(params:DeviceInfo):
    try:
        data = await DeviceController.device_info(params)
        resdata = successResponse(data, message="List of devices")
        return Response(content=json.dumps(resdata,cls=DecimalEncoder), media_type="application/json", status_code=200)
    except ValueError as ve:
        # If there's a ValueError, return a 400 Bad Request with the error message
        raise HTTPException(status_code=400, detail=str(ve))
    except Exception as e:
        # For any other unexpected error, return a 500 Internal Server Error
        raise HTTPException(status_code=500, detail="Internal server error")
    


@api_client_routes.post("/manage/devices/add")
async def add_device(params:List[DeviceAdd]):
    try:
        data = await DeviceController.add_device(params)
        resdata = successResponse(data, message="Device added successfully")
        return Response(content=json.dumps(resdata), media_type="application/json", status_code=200)
    except ValueError as ve:
        raise HTTPException(status_code=400, detail=str(ve))
    except Exception as e:
        raise HTTPException(status_code=500, detail="Internal server error")
    
    
@api_client_routes.post("/manage/devices/edit")
async def edit_device(params:DeviceEdit):
    try:
        data = await DeviceController.edit_device(params)
        resdata = successResponse(data, message="Device edited successfully")
        return Response(content=json.dumps(resdata), media_type="application/json", status_code=200)
    except ValueError as ve:
        raise HTTPException(status_code=400, detail=str(ve))
    except Exception as e:
        raise HTTPException(status_code=500, detail="Internal server error")



@api_client_routes.post("/manage/devices/list")
async def list_device(params:ClientId):
    try:
        data = await DeviceController.manage_list_device(params)
        resdata = successResponse(data, message="List of devices")
        return Response(content=json.dumps(resdata, cls=DecimalEncoder), media_type="application/json", status_code=200)
    except ValueError as ve:
        # If there's a ValueError, return a 400 Bad Request with the error message
        raise HTTPException(status_code=400, detail=str(ve))
    except Exception as e:
        # For any other unexpected error, return a 500 Internal Server Error
        raise HTTPException(status_code=500, detail="Internal server error")

# =================================================================================================
# =================================================================================================
@api_client_routes.post("/devices/energy_data")
async def energy_data(params:EnergyData):
    try:
        data = ClientController.energy_data(params)
        resdata = successResponse(data, message="devices Data")
        return Response(content=json.dumps(resdata,cls=DecimalEncoder), media_type="application/json", status_code=200)
    except ValueError as ve:
        # If there's a ValueError, return a 400 Bad Request with the error message
        raise HTTPException(status_code=400, detail=str(ve))
    except Exception as e:
        # For any other unexpected error, return a 500 Internal Server Error
        raise HTTPException(status_code=500, detail="Internal server error")
    
    
    
    
    
@api_client_routes.post("/devices/graphical_view/energy_used")
async def energy_used(params:EnergyUsed):
    # try:
        data = await DeviceController.energy_used(params)
        resdata = successResponse(data, message="devices Data")
        return Response(content=json.dumps(resdata,cls=DecimalEncoder), media_type="application/json", status_code=200)
    # except ValueError as ve:
    #     raise HTTPException(status_code=400, detail=str(ve))
    # except Exception as e:
    #     raise HTTPException(status_code=500, detail="Internal server error")
    
# =================================================================================================
# =================================================================================================










# =================================================================================================
# =================================================================================================



@api_client_routes.post("/unit/list")
async def list_unit():
    try:
        data = await UnitController.list_unit()
        resdata = successResponse(data, message="List of units")
        return Response(content=json.dumps(resdata), media_type="application/json", status_code=200)
    except ValueError as ve:
        # If there's a ValueError, return a 400 Bad Request with the error message
        raise HTTPException(status_code=400, detail=str(ve))
    except Exception as e:
        # For any other unexpected error, return a 500 Internal Server Error
        raise HTTPException(status_code=500, detail="Internal server error")
    

@api_client_routes.post("/alert/add")
async def add_alert(alert:List[AddAlert]):
    try:
        data = AlertController.add_alert(alert)
        resdata = successResponse(data, message="Alert added successfully")
        print(">>>>>>>>>>>>>>>>>>>>>",resdata)
        return Response(content=json.dumps(resdata,cls=DecimalEncoder), media_type="application/json", status_code=200)
    except ValueError as ve:
        # If there's a ValueError, return a 400 Bad Request with the error message
        raise HTTPException(status_code=400, detail=str(ve))
    except Exception as e:
        # For any other unexpected error, return a 500 Internal Server Error
        raise HTTPException(status_code=500, detail="Internal server error")

@api_client_routes.post("/alert/list")
async def list_alert(params:ClientId):
    try:
        data = await AlertController.list_alert(params)
        resdata = successResponse(data, message="List of alerts")
        return Response(content=json.dumps(resdata,cls=DecimalEncoder), media_type="application/json", status_code=200)
    except ValueError as ve:
        # If there's a ValueError, return a 400 Bad Request with the error message
        raise HTTPException(status_code=400, detail=str(ve))
    except Exception as e:
        # For any other unexpected error, return a 500 Internal Server Error
        raise HTTPException(status_code=500, detail="Internal server error")
    
@api_client_routes.post("/alert/edit")
async def edit_alert(params:EditAlert):
    try:
        data = await AlertController.edit_alert(params)
        resdata = successResponse(data, message="Alert edited successfully")
        return Response(content=json.dumps(resdata), media_type="application/json", status_code=200)
    except ValueError as ve:
        # If there's a ValueError, return a 400 Bad Request with the error message
        raise HTTPException(status_code=400, detail=str(ve))
    except Exception as e:
        # For any other unexpected error, return a 500 Internal Server Error
        raise HTTPException(status_code=500, detail="Internal server error")

@api_client_routes.post("/alert/delete")
async def delete_alert(params:DeleteAlert):
    try:
        data = await AlertController.delete_alert(params)
        if data > 0:
            resdata = successResponse(data, message="Alert deleted successfully")
            return Response(content=json.dumps(resdata), media_type="application/json", status_code=200)
        else:
            resdata = errorResponse(message="Alert not deleted successfully")
            return Response(content=json.dumps(resdata), media_type="application/json", status_code=404)
    except ValueError as ve:
        # If there's a ValueError, return a 400 Bad Request with the error message
        raise HTTPException(status_code=400, detail=str(ve))
    except Exception as e:
        # For any other unexpected error, return a 500 Internal Server Error
        raise HTTPException(status_code=500, detail="Internal server error")