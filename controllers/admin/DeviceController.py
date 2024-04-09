from db_model.MASTER_MODEL import select_data, insert_data,update_data,delete_data,delete_insert_restore,select_one_data

@staticmethod
async def list_device(params):
    try:
        select="device_id, device"
        # select="device_id, device, do_channel, model, lat, lon, imei_no, last_maintenance, DATE_FORMAT(created_at, '%Y-%m-%d %H:%i:%s') AS created_at, DATE_FORMAT(updated_at, '%Y-%m-%d %H:%i:%s') AS updated_at"
        data = select_data("md_device", select)
        return data
    except Exception as e:
        raise e