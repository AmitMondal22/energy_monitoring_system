from pydantic import BaseModel, Field, constr, validator
from datetime import date,datetime,time
import re
from typing import Optional


# class EnergyDeviceData(BaseModel):
#     client_id: int
#     device_id: int
#     device: str
#     do_channel: int
#     device_location: str
#     device_run_hours: float # number of hours the device has been running
#     # device_run_hours: time # time
#     device_dc_bus_voltage: float
#     device_dc_bus_voltage_2: float
#     device_dc_bus_voltage_3: float
#     device_output_current: float
#     device_output_current_2: float
#     device_output_current_3: float
#     device_settings_freq: float
#     device_running_freq: float
#     device_rpm: float
#     device_flow: float


class EnergyDeviceData(BaseModel):
    client_id: int
    device_id: int
    device: str
    do_channel: int
    e1: float
    e2: Optional[float] = None
    e3: Optional[float] = None
    r: float
    y: Optional[float] = None
    b: Optional[float] = None
    r_y: Optional[float] = None
    y_b: Optional[float] = None
    b_y: Optional[float] = None
    curr1: float
    curr2: Optional[float] = None
    curr3: Optional[float] = None
    activep1: float
    activep2: Optional[float] = None
    activep3: Optional[float] = None
    apparentp1: float
    apparentp2: Optional[float] = None
    apparentp3: Optional[float] = None
    pf1: float
    pf2: Optional[float] = None
    pf3: Optional[float] = None
    freq: Optional[float] = None
    reactvp1: float
    reactvp2: Optional[float] = None
    reactvp3: Optional[float] = None
    avaragevln: Optional[float] = None
    avaragevll: Optional[float] = None
    avaragecurrent: Optional[float] = None
    totkw: Optional[float] = None
    totkva: Optional[float] = None
    totkvar: Optional[float] = None
    runhr: Optional[float] = None
    
   
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
    
    
class EnergyUsed(BaseModel):
    client_id: int
    device_id: int
    device: str
    # start_date: date
    # end_date: date
    # start_date_time: datetime = Field(..., alias="start_date_time", description="Format: '%Y-%m-%d %H:%M:%S'")
    start_date_time: datetime
    # end_date_time: datetime
    
    
class VoltageData(BaseModel):
    client_id: int
    device_id: int
    device: str
    start_date_time: datetime
    end_date_time: datetime
    
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
        valid_alert_types = {"3H", "2L", "1CL", "4CH"}
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
    
class EditAlert(BaseModel):
    alert_id: int
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
        valid_alert_types = {"3H", "2L", "1CL", "4CH"}
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

class DeleteAlert(BaseModel):
    alert_id: int
    client_id: int
    organization_id: int
    device_id: int
    
    
class DeviceAdd(BaseModel):
    client_id: int
    device: str
    device_name: str
    do_channel: int
    model: str
    lat: str
    lon: str
    imei_no: str
    last_maintenance: date

class DeviceEdit(BaseModel):
    device_id:int
    client_id: int
    device: str
    device_name: str
    do_channel: int
    model: str
    lat: str
    lon: str
    imei_no: str
    
class UserDeviceList(BaseModel):
    client_id: int
    device_id: int
    device: str
    user_id: int
    organization_id:int