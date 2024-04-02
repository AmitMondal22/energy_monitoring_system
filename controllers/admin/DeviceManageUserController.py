from db_model.MASTER_MODEL import select_data, insert_data,update_data,delete_data,delete_insert_restore,select_one_data
from utils.date_time_format import get_current_datetime

@staticmethod
def add_device(device):
    try:
        current_datetime = get_current_datetime()
        columns = "organization_id, user_id, device_id, created_by, created_at"
        value = f"'{device.organization_id}', '{device.user_id}', '{device.device_id}', '{device.created_by}', '{current_datetime}'"
        device_id = insert_data("md_manage_user_device", columns, value)
        if device_id is None:
            raise ValueError("device registration failed")
        else:
            device_data = {"device_id": device_id, "device_name": device.device_name, "device_info_id": device.device_info_id, "created_by": device.created_by}
            print("device registration successful",device_data)
        return device_data
    except Exception as e:
        raise e
    
    
@staticmethod
def list_user_device():
    try:
        table="md_manage_user_device AS mud, users AS u, md_device AS d, md_organization  AS o"
        select="o.organization_name,o.organization_id,u.user_id,u.user_name,u.user_email,u.user_active_status,d.device_id,d.device,d.do_channel,d.model,d.lat,d.lon,d.imei_no"
        condition=f"mud.user_id = u.user_id AND mud.device_id = d.device_id"
        data = select_data(table, select,condition)
        return data
    except Exception as e:
        raise e

@staticmethod
def edit_device(device):
    try:
        condition = f"manage_user_device_id = {device.manage_user_device_id}"
        columns={"organization_id":{device.organization_id}, "user_id":{device.user_id}, "device_id":{device.device_id}, "created_by":{device.created_by},"updated_at":get_current_datetime()}
        data = update_data("md_device", columns, condition)
        return data
    except Exception as e:
        raise e

@staticmethod
def delete_device(device):
    try:
        condition = f"manage_user_device_id = {device.manage_user_device_id}"
        data = delete_data("md_manage_user_device", condition)
        return data
    except Exception as e:
        raise e