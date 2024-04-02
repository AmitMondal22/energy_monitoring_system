from db_model.MASTER_MODEL import select_data, insert_data,update_data,delete_data,select_one_data
from utils.date_time_format import get_current_datetime,get_current_date,get_current_time


@staticmethod
async def get_energy_data(data):
    try:
        current_datetime = get_current_datetime()
        columns = "device_id, device, do_channel, device_run_hours, device_dc_bus_voltage, device_output_current, device_settings_freq, device_running_freq, device_rpm, device_flow, date, time, created_at"
        value = f"'{data.device_id}', '{data.device}', '{data.do_channel}', {data.device_run_hours}, {data.device_dc_bus_voltage}, {data.device_output_current}, {data.device_settings_freq}, {data.device_running_freq}, {data.device_rpm}, {data.device_flow}, '{get_current_date()}', '{get_current_time()}', '{current_datetime}'"
        device_id = insert_data("td_energy_data", columns, value)
        if device_id is None:
            raise ValueError("device registration failed")
    except Exception as e:
        raise ValueError("Could not fetch data")
 