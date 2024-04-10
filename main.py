from fastapi import FastAPI, HTTPException,WebSocket, WebSocketDisconnect, WebSocket, WebSocketDisconnect
from fastapi.middleware.cors import CORSMiddleware
from fastapi.middleware.trustedhost import TrustedHostMiddleware
import uvicorn
import time

from json import JSONEncoder
from datetime import datetime, date
from routes import api_client_routes, devices_routes, user_routes,auth_routes,mqtt_routes


import paho.mqtt.publish as publish
import paho.mqtt.client as mqtt

from utils.WSPublicConnectionManager import WSPublicConnectionManager



app = FastAPI()
manager = WSPublicConnectionManager()

# MQTT Broker settings
MQTT_BROKER = "techavoiot.co.in"
MQTT_PORT = 1883
MQTT_TOPIC = "test/topic"

# Create MQTT client
mqtt_client = mqtt.Client()

# Set up CORS
origins = [
    "http://192.168.29.210:8000",
    "http://localhost:8000",
    "*"
]

# @app.middleware("http")
# Apply TrustedHost middleware to the main FastAPI app
app.add_middleware(TrustedHostMiddleware, allowed_hosts=["*"])

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)



# # =============================================
#             # mqtt
# # =============================================
# # MQTT on_connect callback
# def on_connect(client, userdata, flags, rc):
#     print("Connected with result code "+str(rc))
#     client.subscribe(MQTT_TOPIC)
    
# # MQTT on_message callback
# def on_message(client, userdata, msg):
#     print(msg.topic+" "+str(msg.payload))

# # Set the callback functions
# mqtt_client.on_connect = on_connect
# mqtt_client.on_message = on_message

# # Connect to MQTT Broker
# mqtt_client.connect(MQTT_BROKER, MQTT_PORT, 60)
# mqtt_client.loop_start()  # Start the loop to listen for MQTT messages


# @app.post("/publish/")
# async def publish_message(message_data: dict):
#     try:
#         # publish.single(MQTT_TOPIC, message, hostname=MQTT_BROKER)
#         # return {"message": "Published message: {}".format(message)}
        
#         message = message_data
#         if message:
#             mqtt_client.publish(MQTT_TOPIC, message)
#             return {"message": "Published message: {}".format(message)}
#         else:
#             return {"error": "Message not provided in JSON data"}
        
#         # mqtt_client.publish(MQTT_TOPIC, message)
#         # return {"message": "Published message: {}".format(message)}
#     except Exception as e:
#         return {"error": str(e)}





# # @app.websocket("/wsmqtt")
# # async def websocket_endpoint(websocket: WebSocket):
# #     await manager.self_connect(websocket)
    
# #     try:
# #         while True:
# #             message = mqtt_client.loop()
# #             if message:
# #                 data = await websocket.receive_text()
# #                 await manager.self_send_personal_message(f"Received:{data}",websocket)
# #     except WebSocketDisconnect:
# #         manager.self_disconnect(websocket)
# #         await manager.self_send_personal_message("Bye!!!",websocket)
        


        
# @app.websocket("/wsmqtt")
# async def websocket_endpoint(websocket: WebSocket):
#     await manager.self_connect(websocket)
#     try:
#         while True:
#             mqtt_client.loop_start()
#             time.sleep(1)
#     except WebSocketDisconnect:
#         manager.self_disconnect(websocket)
#         await manager.self_send_personal_message("Bye!!!", websocket)
#     finally:
#         mqtt_client.disconnect()
        

# @app.websocket("/subscribe_mqtt")
# async def websocket_endpoint(websocket: WebSocket):
#     try:
#         await websocket.accept()
#         while True:
#             message = mqtt_client.loop()
#             if message:
#                 await websocket.send_text(message)
#     except WebSocketDisconnect:
#         await websocket.remove(websocket)
#         await websocket.send_text("Bye!!!",websocket)


# # =============================================
# # =============================================



# Custom JSON encoder
class CustomJSONEncoder(JSONEncoder):
    def default(self, obj):
        if isinstance(obj, datetime):
            return obj.strftime('%Y-%m-%d %H:%M:%S')
        return super().default(obj)

# Set the custom JSON encoder for FastAPI
app.json_encoder = CustomJSONEncoder



# Include user routes
app.include_router(auth_routes.auth_routes, prefix="/api/auth", tags=["auth"])

# Include user routes
app.include_router(user_routes.user_rutes, prefix="/api/user", tags=["user"])

# Include user routes
app.include_router(devices_routes.devices_routes, prefix="/api/device", tags=["device"])


# Include user routes
app.include_router(api_client_routes.api_client_routes, prefix="/api/client", tags=["client"])



# Include user routes
app.include_router(mqtt_routes.mqtt_routes, prefix="/api/mqtt", tags=["mqtt"])

# Index route
@app.get('/')
def index():
    return "hello world"  # Corrected typo


if __name__ == "__main__":
    
    # Run the FastAPI application
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)
    

    
    
    
