from db_model.MASTER_MODEL import select_data, insert_data,batch_insert_data
from utils.date_time_format import get_current_datetime

def add_alert(data):
    try:

        column="client_id, organization_id, device_id, device, unit_id, alert_type, alert_status, alert_value,alert_email,create_by,created_at"
        # row_data=f"{data.client_id},{data.organization_id},{data.device_id}, '{data.device}', {data.unit_id}, '{data.alert_type}', '{data.alert_status}', {data.alert_value},'{data.alert_email}',{data.create_by},'{get_current_datetime()}'"
        # alert_id=insert_data("td_alert", column,row_data)
        
        
        
        # rows_data = [{"name": "John", "email": "john@example.com"}, {"name": "Alice", "email": "alice@example.com"}]
        
        rows_data = []
        for entry in data:
            row_data = {
                "client_id": entry.client_id,
                "organization_id": entry.organization_id,
                "device_id": entry.device_id,
                "device": entry.device,
                "unit_id": entry.unit_id,
                "alert_type": entry.alert_type,
                "alert_status": entry.alert_status,
                "alert_value": entry.alert_value,
                "alert_email": entry.alert_email,
                "create_by": entry.create_by,
                "created_at": get_current_datetime()  # Assuming get_current_datetime() returns the current datetime
            }
            rows_data.append(row_data)
        
       
        
        print("row_data_list---------------------", rows_data)
        # row_data=f"{data.client_id},{data.organization_id},{data.device_id}, '{data.device}', {data.unit_id}, '{data.alert_type}', '{data.alert_status}', {data.alert_value},'{data.alert_email}',{data.create_by},'{get_current_datetime()}'"
        
        batch_dataid=batch_insert_data("td_alert", column, rows_data)
        print("batch_dataid---------------------", batch_dataid)
        return batch_dataid
    except Exception as e:
        raise e