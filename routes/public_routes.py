from fastapi import APIRouter, HTTPException, Response, Depends, Request
from utils.response import errorResponse, successResponse
from models import device_data_model
from controllers.device_to_server import EnergyController
import json
public_routes = APIRouter()



@public_routes.get('/energy_data/devices_to_storage')
async def get_energy_data(data:device_data_model.EnergyDeviceData):
    try:
        controllerRes = await EnergyController.get_energy_data(data)   
        resdata = successResponse(controllerRes, message="User registered successfully")
        return Response(content=json.dumps(resdata), media_type="application/json", status_code=200)
    except ValueError as ve:
        raise HTTPException(status_code=400, detail=str(ve))
    except Exception as e:
        raise HTTPException(status_code=500, detail="Internal server error")