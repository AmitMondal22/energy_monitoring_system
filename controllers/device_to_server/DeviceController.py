from db_model.MASTER_MODEL import select_data, insert_data,update_data,delete_data,select_one_data,select_last_data
from utils.date_time_format import get_current_datetime,get_current_date,get_current_time
from utils.utils import increment_string



   
@staticmethod
async def device_auto_register(data):
    try:
        select="device_id, device, do_channel, model, lat, lon, imei_no, last_maintenance, DATE_FORMAT(created_at, '%Y-%m-%d %H:%i:%s') AS created_at, DATE_FORMAT(updated_at, '%Y-%m-%d %H:%i:%s') AS updated_at"
        find_device=select_one_data("md_device", select, f"imei_no = '{data.imei_no}'")

        if find_device is not None:
            device_data={"device": find_device['device'], "do_channel": find_device['do_channel'], "model": find_device['model'], "lat": find_device['lat'], "lon": find_device['lon'], "imei_no": find_device['imei_no'], "created_at": find_device['created_at'], "updated_at": find_device['updated_at']}
            return device_data
        
        device_name = select_last_data("md_device", select,None,"created_at")
        if device_name is not None:
            u_id = increment_string(device_name['device'])
            
        else:
            # u_id = "C1TS00000001"
            u_id = "IB00000001"
        current_datetime = get_current_datetime()
        columns = "device, do_channel, model, lat, lon, imei_no, created_at"
        value = f"'{u_id}', '{data.do_channel}', '{data.model}', '{data.lat}', '{data.lon}', '{data.imei_no}', '{current_datetime}'"
        device_id = insert_data("md_device", columns, value)
        if device_id is None:
            raise ValueError("device registration failed")
        else:
            device_data = {"device_id": device_id, "device_name": u_id, "do_channel": data.do_channel, "model": data.model, "lat": data.lat, "lon": data.lon, "imei_no": data.imei_no, "created_at": current_datetime}
        return device_data
    except Exception as e:
        raise ValueError("Could not fetch data")
    
@staticmethod
async def checked_devices(data):
    try:
        select="device_id, device, do_channel, model, lat, lon, imei_no, last_maintenance, DATE_FORMAT(created_at, '%Y-%m-%d %H:%i:%s') AS created_at, DATE_FORMAT(updated_at, '%Y-%m-%d %H:%i:%s') AS updated_at"
        condition = f"device = '{data.device}'"
        find_devices=select_one_data("md_device", select, condition,None)
        print("find_devices>>>>>>>>>>>>>>>>>",find_devices)
        if find_devices is not None:
            device_data={"device": find_devices['device'], "do_channel": find_devices['do_channel'], "model": find_devices['model'], "lat": find_devices['lat'], "lon": find_devices['lon'], "imei_no": find_devices['imei_no'], "created_at": find_devices['created_at'], "updated_at": find_devices['updated_at']}
            return device_data
        else:
            return "Device not found"
    except Exception as e:
        raise ValueError("Could not fetch data")