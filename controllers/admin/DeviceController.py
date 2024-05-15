from db_model.MASTER_MODEL import select_data,update_data,select_one_data,batch_insert_data
from utils.date_time_format import get_current_datetime, get_current_date_time_utc


@staticmethod
async def list_device(client_id):
    try:
        select="device_id, device,device_type,meter_type"
        # select="device_id, device, do_channel, model, lat, lon, imei_no, last_maintenance, DATE_FORMAT(created_at, '%Y-%m-%d %H:%i:%s') AS created_at, DATE_FORMAT(updated_at, '%Y-%m-%d %H:%i:%s') AS updated_at"
        condition=f"client_id={client_id} AND device_type='EN'"
        data = select_data("md_device", select, condition)
        return data
    except Exception as e:
        raise e
    
    
@staticmethod
async def user_device_list(client_id, user_id, organization_id):
    try:
        select="d.device_id, d.device, d.do_channel, d.model, d.lat, d.lon, d.imei_no,d.device_type,d.meter_type, d.last_maintenance, DATE_FORMAT(d.created_at, '%Y-%m-%d %H:%i:%s') AS created_at, DATE_FORMAT(d.updated_at, '%Y-%m-%d %H:%i:%s') AS updated_at"
        
        condition = f"d.device_id = mud.device_id AND d.client_id = mud.client_id AND mud.client_id = {client_id} AND mud.user_id = {user_id} AND mud.organization_id = {organization_id} AND d.device_type='EN'"
        find_devices=select_data("md_device AS d, md_manage_user_device AS mud", select, condition,None)
        print("find_devices>>>>>>>>>>>>>>>>>",find_devices)
        return find_devices
    except Exception as e:
        raise ValueError("Could not fetch data")


@staticmethod
async def device_info(params):
    try:
        condition = f"client_id={params.client_id} AND device_id = {params.device_id} AND device_type='EN'"
        select="device_id, client_id, device, device_name, do_channel, model, lat, lon, imei_no, last_maintenance,device_type,meter_type, DATE_FORMAT(created_at, '%Y-%m-%d %H:%i:%s') AS created_at, DATE_FORMAT(updated_at, '%Y-%m-%d %H:%i:%s') AS updated_at"
        data = select_one_data("md_device",select, condition,order_by="device_id DESC")
        
        select2="count(a.alert_id) alert, a.alert_type, a.unit_id,u.unit,u.unit_name"
        condition2 = f"a.unit_id=u.unit_id AND a.client_id={params.client_id} AND a.device_id = {params.device_id} GROUP BY a.alert_type, a.unit_id, u.unit, u.unit_name"
        table2="td_alert AS a, md_unit AS u"
        alert=select_data(table2,select2, condition2)
        return {"data":data, "data2":alert}
    except Exception as e:
        raise e

@staticmethod
async def add_device(params):
    try:
        
        
        column="client_id, device, device_name, do_channel, model, lat, lon, imei_no, device_type, meter_type, last_maintenance, created_at"
        
        rows_data = []
        for params_data in params:
            row_data = {
                "client_id": params_data.client_id,
                "device": params_data.device,
                "device_name": params_data.device_name,
                "do_channel": params_data.do_channel,
                "model": params_data.model,
                "lat": params_data.lat,
                "lon": params_data.lon,
                "imei_no": params_data.imei_no,
                "device_type": params_data.device_type,
                "meter_type": params_data.meter_type,
                "last_maintenance": params_data.last_maintenance,
                "created_at": get_current_datetime()  # Assuming get_current_datetime() returns the current datetime
            }
            rows_data.append(row_data)        
        batch_dataid=batch_insert_data("md_device", column, rows_data)
        print("batch_dataid---------------------", batch_dataid)
        return batch_dataid
    except Exception as e:
        raise e
    
@staticmethod
async def edit_device(params):
    try:
        condition = f"device_id = {params.device_id} AND client_id = {params.client_id}"
        columns={"device":params.device, "device_name":params.device_name, "do_channel":params.do_channel, "model":params.model, "lat":params.lat, "lon":params.lon, "imei_no":params.imei_no, "device_type" :params.device_type, "meter_type":params.meter_type, "updated_at":get_current_datetime()}
        data = update_data("md_device", columns, condition)
        print(data)
        return data
    except Exception as e:
        raise e
    

@staticmethod
async def manage_list_device(params):
    try:
        condition = f"a.client_id = {params.client_id} AND a.device_type='EN'"
        
        select="a.device_id, a.client_id, a.device, a.device_name, a.do_channel, a.model, a.lat, a.lon, a.imei_no, a.device_type,a.meter_type,a.last_maintenance, DATE_FORMAT(a.created_at, '%Y-%m-%d') AS device_created_at,DATE_FORMAT(a.updated_at, '%Y-%m-%d %H:%i:%s') AS device_updated_at, b.energy_data_id, b.device_id AS b_device_id, b.do_channel AS b_do_channel, b.e1, b.e2, b.e3, b.r, b.y, b.b, b.r_y, b.y_b, b.b_r, b.curr1, b.curr2, b.curr3, b.activep1, b.activep2, b.activep3, b.apparentp1, b.apparentp2, b.apparentp3, b.pf1, b.pf2, b.pf3, b.freq, b.reactvp1, b.reactvp2, b.reactvp3, b.avaragevln, b.avaragevll, b.avaragecurrent, b.totkw, b.totkva, b.totkvar, b.runhr,  DATE_FORMAT(b.date, '%Y-%m-%d') AS date, TIME_FORMAT(b.time, '%H:%i:%s') AS time, DATE_FORMAT(b.created_at, '%Y-%m-%d %H:%i:%s') AS energy_data_created_at, DATE_FORMAT(b.updated_at, '%Y-%m-%d %H:%i:%s') AS energy_data_updated_at"
        
        table="md_device a LEFT JOIN (SELECT * FROM td_energy_data ORDER BY date DESC, time DESC) b ON a.device_id = b.device_id AND a.client_id = b.client_id"
        
        order_by="a.device_id ASC"
        data = select_data(table, select,condition,order_by)
        print("????????????????>>>>>>>>>>>>>>>>",data)
        return data
    except Exception as e:
        raise e
    



    
# =========================================================
@staticmethod
async def energy_used(params):
    try:
       
        end_date_time=get_current_date_time_utc()
        start_date_time=params.start_date_time
       
        
        condition = f"client_id = {params.client_id} AND device_id = {params.device_id} AND created_at BETWEEN '{start_date_time.strftime('%Y-%m-%d %H:%M:%S')}' AND '{end_date_time}'"
        select="energy_data_id, device_id, do_channel, e1, e2, e3, DATE_FORMAT(date, '%Y-%m-%d') AS date, TIME_FORMAT(time, '%H:%i:%s') AS time, DATE_FORMAT(created_at, '%Y-%m-%d %H:%i:%s') AS created_at, DATE_FORMAT(updated_at, '%Y-%m-%d %H:%i:%s') AS updated_at"
        data = select_data("td_energy_data",select, condition,order_by="energy_data_id DESC")
        return data
    except Exception as e:
        raise e
    
@staticmethod
async def voltage_data(params):
    try:
        end_date_time=params.end_date_time
        start_date_time=params.start_date_time
        
        condition = f"client_id = {params.client_id} AND device_id = {params.device_id} AND created_at BETWEEN '{start_date_time.strftime('%Y-%m-%d %H:%M:%S')}' AND '{end_date_time.strftime('%Y-%m-%d %H:%M:%S')}'"
        select="energy_data_id, device_id, do_channel, r, y, b, r_y, y_b, b_r, DATE_FORMAT(date, '%Y-%m-%d') AS date, TIME_FORMAT(time, '%H:%i:%s') AS time, DATE_FORMAT(created_at, '%Y-%m-%d %H:%i:%s') AS created_at, DATE_FORMAT(updated_at, '%Y-%m-%d %H:%i:%s') AS updated_at"
        data = select_data("td_energy_data",select, condition,order_by="energy_data_id DESC")
        return data
    except Exception as e:
        raise e

@staticmethod
async def current_data(params):
    try:
        end_date_time=params.end_date_time
        start_date_time=params.start_date_time
        
        condition = f"client_id = {params.client_id} AND device_id = {params.device_id} AND created_at BETWEEN '{start_date_time.strftime('%Y-%m-%d %H:%M:%S')}' AND '{end_date_time.strftime('%Y-%m-%d %H:%M:%S')}'"
        select="energy_data_id, device_id, do_channel, curr1, curr2, curr3, DATE_FORMAT(date, '%Y-%m-%d') AS date, TIME_FORMAT(time, '%H:%i:%s') AS time, DATE_FORMAT(created_at, '%Y-%m-%d %H:%i:%s') AS created_at, DATE_FORMAT(updated_at, '%Y-%m-%d %H:%i:%s') AS updated_at"
        data = select_data("td_energy_data",select, condition,order_by="energy_data_id DESC")
        return data
    except Exception as e:
        raise e
    
    
@staticmethod
async def power_data(params):
    try:
        end_date_time=params.end_date_time
        start_date_time=params.start_date_time
    
        condition = f"client_id = {params.client_id} AND device_id = {params.device_id} AND created_at BETWEEN '{start_date_time.strftime('%Y-%m-%d %H:%M:%S')}' AND '{end_date_time.strftime('%Y-%m-%d %H:%M:%S')}'"
        select="energy_data_id, device_id, do_channel, activep1, activep2, activep3, apparentp1, apparentp2, apparentp3, pf1, pf2, pf3, DATE_FORMAT(date, '%Y-%m-%d') AS date, TIME_FORMAT(time, '%H:%i:%s') AS time, DATE_FORMAT(created_at, '%Y-%m-%d %H:%i:%s') AS created_at, DATE_FORMAT(updated_at, '%Y-%m-%d %H:%i:%s') AS updated_at"
        data = select_data("td_energy_data",select, condition,order_by="energy_data_id DESC")
        return data
    except Exception as e:
        raise e
    
@staticmethod
async def total_power_analisis(params):
    try:
        end_date_time=params.end_date_time
        start_date_time=params.start_date_time
        
        condition = f"client_id = {params.client_id} AND device_id = {params.device_id} AND created_at BETWEEN '{start_date_time.strftime('%Y-%m-%d %H:%M:%S')}' AND '{end_date_time.strftime('%Y-%m-%d %H:%M:%S')}'"
        select="energy_data_id, device_id, do_channel, totkw, totkva, totkvar, runhr, DATE_FORMAT(date, '%Y-%m-%d') AS date, TIME_FORMAT(time, '%H:%i:%s') AS time, DATE_FORMAT(created_at, '%Y-%m-%d %H:%i:%s') AS created_at, DATE_FORMAT(updated_at, '%Y-%m-%d %H:%i:%s') AS updated_at"
        data = select_data("td_energy_data",select, condition,order_by="energy_data_id DESC")
        return data
    except Exception as e:
        raise e