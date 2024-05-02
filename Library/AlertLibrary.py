from db_model.MASTER_MODEL import select_data, insert_data,update_data,delete_data,select_one_data,select_last_data

async def send_alert(client_id, device_id, device, data):
    try:
        print(data)
        print("=====================???????????")
        select="alert_id, client_id, organization_id, device_id, device, units, alert_type, alert_value, alert_status, DATE_FORMAT(created_at, '%Y-%m-%d %H:%i:%s') AS created_at"
        
        
        
        table = "td_alert AS a, md_unit AS b"
        
        
        
        
        condition=f"a.unit_id=b.unit_id AND a.client_id={client_id} AND a.device_id='{device_id}' AND a.device='{device}' AND a.alert_status='Active' AND a.alert_value{data['condition']} {data['value']}"
        
        
        
        alertdata=select_data(table,select,condition)
        
    except Exception as e:
        print(e)