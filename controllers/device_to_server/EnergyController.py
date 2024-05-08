from db_model.MASTER_MODEL import select_data, insert_data,update_data,delete_data,select_one_data,custom_select_sql_query
from utils.date_time_format import get_current_datetime,get_current_date,get_current_time
from fastapi import BackgroundTasks
from Library.DecimalEncoder import DecimalEncoder
from Library import AlertLibrary
import json
from Library.MqttLibraryClass import MqttLibraryClass


from hooks.update_event_hooks import update_topics

@staticmethod
async def get_energy_data(data):
    try:
        current_datetime = get_current_datetime()
        columns = "client_id, device_id, device, do_channel,e1, e2, e3, r, y, b, r_y, y_b, b_y, curr1, curr2, curr3, activep1, activep2, activep3, apparentp1, apparentp2, apparentp3, pf1, pf2, pf3, freq, reactvp1, reactvp2, reactvp3, avaragevln, avaragevll, avaragecurrent, totkw, totkva, totkvar, runhr, date, time, created_at"
        value = f"{data.client_id}, {data.device_id}, '{data.device}', {data.do_channel}, {data.e1}, {data.e2}, {data.e3}, {data.r}, {data.y}, {data.b}, {data.r_y}, {data.y_b}, {data.b_y}, {data.curr1}, {data.curr2}, {data.curr3}, {data.activep1}, {data.activep2}, {data.activep3}, {data.apparentp1}, {data.apparentp2}, {data.apparentp3}, {data.pf1}, {data.pf2}, {data.pf3}, {data.freq}, {data.reactvp1}, {data.reactvp2}, {data.reactvp3}, {data.avaragevln}, {data.avaragevll}, {data.avaragecurrent}, {data.totkw}, {data.totkva}, {data.totkvar}, {data.runhr}, '{get_current_date()}', '{get_current_time()}', '{current_datetime}'"
        energy_data_id = insert_data("td_energy_data", columns, value)
        
        
        
        # mqtt_client = MqttLibraryClass("techavoiot.co.in", 1883)
        # # Connect to the MQTT broker
        # mqtt_client.connect()
        
        # data=await update_topics()
        # print("data",data)
        # mqtt_client.subscribe(data)
        
        
        
        
        if energy_data_id is None:
            raise ValueError("energy data was not inserted")
        else:
            # from routes.api_client_routes import SendEnergySocket
            # lastdata=await SendEnergySocket.send_last_energy_data(data.client_id, data.device_id, data.device)
            lastdata=await send_last_energy_data(data.client_id, data.device_id, data.device)
            if lastdata is None:
                raise ValueError("Could not fetch data")
            user_data = {"energy_data_id":energy_data_id, "device_id": data.device_id, "device": data.device, "do_channel": data.do_channel}
        return user_data
    except Exception as e:
        raise ValueError("Could not fetch data")
    
    

@staticmethod  
async def send_last_energy_data(client_id, device_id, device):
        try:
            # Lazy import inside the function
            from Library.WsConnectionManagerManyDeviceTypes import WsConnectionManagerManyDeviceTypes
            manager = WsConnectionManagerManyDeviceTypes()
            background_tasks = BackgroundTasks()
            from routes.ws_routes import sennd_ws_message            
            custom_sql=f""" SELECT 
                                td.energy_data_id, 
                                td.client_id, 
                                td.device_id, 
                                td.device, 
                                td.do_channel, 
                                td.e1, 
                                td.e2, 
                                td.e3, 
                                td.r, 
                                td.y, 
                                td.b, 
                                td.r_y, 
                                td.y_b, 
                                td.b_y, 
                                td.curr1, 
                                td.curr2, 
                                td.curr3, 
                                td.activep1, 
                                td.activep2, 
                                td.activep3, 
                                td.apparentp1, 
                                td.apparentp2, 
                                td.apparentp3, 
                                td.pf1, 
                                td.pf2, 
                                td.pf3, 
                                td.freq, 
                                td.reactvp1, 
                                td.reactvp2, 
                                td.reactvp3, 
                                td.avaragevln, 
                                td.avaragevll, 
                                td.avaragecurrent, 
                                td.totkw, 
                                td.totkva, 
                                td.totkvar, 
                                td.runhr, 
                                td.date, 
                                td.time, 
                                DATE_FORMAT(td.created_at, '%Y-%m-%d %H:%i:%s') AS created_at,
                                (SELECT MAX(e1) FROM td_energy_data WHERE DATE(date) = DATE_SUB(CURDATE(), INTERVAL 1 DAY) AND device_id = td.device_id AND client_id = td.client_id AND device = td.device) AS e1_yesterday,
                                (SELECT MAX(e2) FROM td_energy_data WHERE DATE(date) = DATE_SUB(CURDATE(), INTERVAL 1 DAY) AND device_id = td.device_id AND client_id = td.client_id AND device = td.device) AS e2_yesterday,
                                (SELECT MAX(e3) FROM td_energy_data WHERE DATE(date) = DATE_SUB(CURDATE(), INTERVAL 1 DAY) AND device_id = td.device_id AND client_id = td.client_id AND device = td.device) AS e3_yesterday,
                                (SELECT MAX(e1) FROM td_energy_data WHERE DATE(date) >= DATE_SUB(CURDATE(), INTERVAL 30 DAY) AND device_id = td.device_id AND client_id = td.client_id AND device = td.device) AS e1_past_month,
                                (SELECT MAX(e2) FROM td_energy_data WHERE DATE(date) >= DATE_SUB(CURDATE(), INTERVAL 30 DAY) AND device_id = td.device_id AND client_id = td.client_id AND device = td.device) AS e2_past_month,
                                (SELECT MAX(e3) FROM td_energy_data WHERE DATE(date) >= DATE_SUB(CURDATE(), INTERVAL 30 DAY) AND device_id = td.device_id AND client_id = td.client_id AND device = td.device) AS e3_past_month,
                                (SELECT MAX(e1) FROM td_energy_data WHERE YEAR(date) = YEAR(CURDATE())-1 AND device_id = td.device_id AND client_id = td.client_id AND device = td.device) AS e1_past_year,
                                (SELECT MAX(e2) FROM td_energy_data WHERE YEAR(date) = YEAR(CURDATE())-1 AND device_id = td.device_id AND client_id = td.client_id AND device = td.device) AS e2_past_year,
                                (SELECT MAX(e3) FROM td_energy_data WHERE YEAR(date) = YEAR(CURDATE())-1 AND device_id = td.device_id AND client_id = td.client_id AND device = td.device) AS e3_past_year
                            FROM 
                                td_energy_data td
                            WHERE 
                                td.device_id = '{device_id}'
                                AND td.device = '{device}'
                                AND td.client_id = '{client_id}'
                            ORDER BY 
                                td.energy_data_id DESC """
            lastdata=custom_select_sql_query(custom_sql,None)
            print("TTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTT",json.dumps(lastdata, cls=DecimalEncoder))
            background_tasks.add_task(AlertLibrary.send_alert, client_id, device_id, device, json.dumps(lastdata, cls=DecimalEncoder))

            await sennd_ws_message("EMS",client_id, device_id, device, json.dumps(lastdata, cls=DecimalEncoder))
            
            print("lastdata last energy data>>>>>>>>>>/////////",json.dumps(lastdata, cls=DecimalEncoder))
            return json.dumps(lastdata, cls=DecimalEncoder)
        except Exception as e:
            raise ValueError("Could not fetch data")
    
    
