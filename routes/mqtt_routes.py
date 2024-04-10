from fastapi import APIRouter, HTTPException,Response
from controllers.user import UserController

from Library.MqttLibrary import mqtt_client, MQTT_TOPIC,publish_energy_message
from Library.MqttLibraryClass import MqttLibraryClass


from utils.response import errorResponse, successResponse
import json

from models.mqtt_model import MqttEnergyDeviceData
mqtt_routes = APIRouter()




mqtt_client = MqttLibraryClass("techavoiot.co.in", 1883)
mqtt_client.start_loop()


@mqtt_routes.on_event("startup")
async def startup_event():
    mqtt_client.set_topic("test/topicaa")
    print("Subscribed to topic:", mqtt_client.topic)
    
    
    

@mqtt_routes.post("/publish/")
async def publish_message(message_data: MqttEnergyDeviceData):
    try:
        
        # mqtt_client = MqttLibraryClass("test/topic")
        mqtt_client = MqttLibraryClass("techavoiot.co.in", 1883, "test/topic")
        data=await mqtt_client.publish_message(message_data)
       
        resdata = successResponse(data, message="energy data published successfully")
        return Response(content=json.dumps(resdata), media_type="application/json", status_code=200)
    except Exception as e:
        return {"error": str(e)}


def on_message(client, userdata, msg):
    # This function will be called whenever a new message is received
    print(f"Received message: {msg.payload.decode()} from topic {msg.topic}")


@mqtt_routes.post("/publish2/")
async def publish_message(topic: str, message: str):
    try:
        data = mqtt_client.publish_message(topic, message)
        return {"message": "Published message successfully"}
    except Exception as e:
        return {"error": str(e)}