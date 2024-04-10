from pydantic import BaseModel, Field, constr, validator
from datetime import date,datetime,time

class MqttEnergyDeviceData(BaseModel):
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
    