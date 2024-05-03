from db_model.MASTER_MODEL import select_data, insert_data,update_data,delete_data,select_one_data
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
        columns = "client_id, device_id, device, do_channel, device_run_hours, device_dc_bus_voltage,device_dc_bus_voltage2,device_dc_bus_voltage3, device_output_current,device_output_current2,device_output_current3, device_settings_freq, device_running_freq, device_rpm, device_flow, date, time, created_at"
        value = f"{data.client_id},{data.device_id}, '{data.device}', {data.do_channel}, {data.device_run_hours},{data.device_dc_bus_voltage},{data.device_dc_bus_voltage_2},{data.device_dc_bus_voltage_3}, {data.device_output_current},{data.device_output_current_2},{data.device_output_current_3}, {data.device_settings_freq}, {data.device_running_freq}, {data.device_rpm}, {data.device_flow}, '{get_current_date()}', '{get_current_time()}', '{current_datetime}'"
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
async def send_last_energy_data(client_id, device_id, device, background_tasks: BackgroundTasks):
        try:
            # Lazy import inside the function
            from Library.WsConnectionManagerManyDeviceTypes import WsConnectionManagerManyDeviceTypes
            manager = WsConnectionManagerManyDeviceTypes()
            
            select="energy_data_id, client_id, device_id, device, do_channel, device_run_hours, device_dc_bus_voltage,device_dc_bus_voltage2,device_dc_bus_voltage3, device_output_current,device_output_current2,device_output_current3, device_settings_freq, device_running_freq, device_rpm, device_flow, date, time, DATE_FORMAT(created_at, '%Y-%m-%d %H:%i:%s') AS created_at"
            condition = f"device_id = '{device_id}' AND device ='{device}' AND client_id = '{client_id}'"
            order_by="energy_data_id DESC"
                
            lastdata = select_one_data("td_energy_data", select, condition, order_by)
           
           
            # AlertLibrary.send_alert(client_id, device_id, device, json.dumps(lastdata, cls=DecimalEncoder))
            #background_tasks.add_task(AlertLibrary.send_alert(client_id, device_id, device, json.dumps(lastdata, cls=DecimalEncoder)))
            
            
            background_tasks.add_task(AlertLibrary.send_alert, client_id, device_id, device, json.dumps(lastdata, cls=DecimalEncoder))
            
            
            await manager.send_personal_message("EMS",client_id, device_id, device, json.dumps(lastdata, cls=DecimalEncoder))
            
            print("lastdata last energy data>>>>>>>>>>/////////",json.dumps(lastdata, cls=DecimalEncoder))
            return json.dumps(lastdata, cls=DecimalEncoder)
        except Exception as e:
            raise ValueError("Could not fetch data")
    
    
 
# @staticmethod
# async def send_last_energy_data(client_id, device_id, device):
#     try:
#          # Lazy import inside the function
#         from Library import WsConnectionManager
#         manager = WsConnectionManager.WsConnectionManager()
        
#         select="energy_data_id, client_id, device_id, device, do_channel, device_run_hours, device_dc_bus_voltage, device_output_current, device_settings_freq, device_running_freq, device_rpm, device_flow, date, time, DATE_FORMAT(created_at, '%Y-%m-%d %H:%i:%s') AS created_at"
#         condition = f"device_id = '{device_id}' AND device ='{device}' AND client_id = '{client_id}'"
#         order_by="energy_data_id DESC"
            
#         lastdata = select_one_data("td_energy_data", select, condition, order_by)
            
       
#         # await manager.send_personal_message(client_id, device_id, device, json.dumps(lastdata, cls=DecimalEncoder))
        
#         # await manager.send_personal_message(client_id, device_id, device, json.dumps("hello134"))
        
        
#         abc=await manager.send_personal_message(1, 1, "aa", json.dumps("hello world"))
#         print("lastdata last energy data>>>>>>>>>>/////////",lastdata)
#         return lastdata
#     except Exception as e:
#         raise ValueError("Could not fetch data")


# @staticmethod
# async def send_last_energy_data(client_id, device_id, device):
#     try:
#         # Lazy import inside the function
#         from Library import WsConnectionManager
#         manager = WsConnectionManager.WsConnectionManager()
        
#         user_id = f"{client_id}-{device_id}-{device}"
        
#         # Check if the user_id is in active_connections
#         if user_id in manager.active_connections:
#             # If the user_id is found, send the message
#             await manager.send_personal_message(client_id, device_id, device, json.dumps("hello world"))
#             print("Message sent successfully")
#         else:
#             # If the user_id is not found, connect the user
#             websocket = await manager.connect(client_id, device_id, device)
#             if websocket:
#                 # If connection successful, send the message
#                 await manager.send_personal_message(client_id, device_id, device, json.dumps("hello world"))
#                 print("User connected and message sent successfully")
#             else:
#                 print("Failed to establish connection for user")
#     except Exception as e:
#         raise ValueError("Could not fetch data")