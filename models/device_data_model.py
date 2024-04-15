from pydantic import BaseModel, Field, constr, validator
from datetime import date,datetime,time


class EnergyDeviceData(BaseModel):
    client_id: int
    device_id: str
    device: str
    do_channel: str
    device_type: str
    device_location: str
    device_run_hours: float # number of hours the device has been running
    # device_run_hours: time # time
    device_dc_bus_voltage: float
    device_output_current: float
    device_settings_freq: float
    device_running_freq: float
    device_rpm: float
    device_flow: float
    
   
# $flow=(round((100*$r->rpm)/2800, 2) >100)?100:round((100*$r->rpm)/2800, 2);


class DeviceAutoRegister(BaseModel):
    do_channel:str
    model:str
    lat:str
    lon:str
    imei_no:str


class CheckedDevices(BaseModel):
    device:str
    
class EnergyData(BaseModel):
    client_id: int
    device_id: int
    device: str
    start_date: date
    end_date: date
    
class WsEnergyData(BaseModel):
    client_id: int
    device_id: int
    device: str