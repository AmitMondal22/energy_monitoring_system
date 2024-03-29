from pydantic import BaseModel, Field, constr, validator
from datetime import date,datetime,time


class EnergyDeviceData(BaseModel):
    device_id: str
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
