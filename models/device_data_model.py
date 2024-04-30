from pydantic import BaseModel, Field, constr, validator
from datetime import date,datetime,time
import re


class EnergyDeviceData(BaseModel):
    client_id: int
    device_id: int
    device: str
    do_channel: int
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
    # client_id: int
    ib_id: int
    # device_id: int
    do_channel:int
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
    
    
    
# ==========================================
# ==========================================



class UpsDeviceData(BaseModel):
    client_id: int
    device_id: int
    device: str
    do_channel: int
    device_location: str
    device_output_current: float
    device_input_current: float
    
    
    
# ========================================

class AddAlert(BaseModel):
    client_id: int
    organization_id: int
    device_id: int
    device: str
    unit_id: int
    alert_type: str
    alert_status: str
    alert_status: str
    alert_value: float
    alert_email : str
    create_by: int
    @validator('alert_type')
    def validate_alert_type(cls, v):
        valid_alert_types = {"H", "L", "CL", "CH"}
        if v not in valid_alert_types:
            raise ValueError('Invalid alert type')
        return v
    @validator('alert_status')
    def validate_alert_status(cls, v):
        valid_alert_status = {"Y", "N"}
        if v not in valid_alert_status:
            raise ValueError('Invalid alert status')
        return v
    @validator('alert_email')
    def validate_email(cls, alert_email):
        # Regular expression for basic email validation
        pattern = r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$"
        if not re.match(pattern, alert_email):
            raise ValueError("Invalid email address")
        return alert_email
