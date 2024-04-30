import logging
async def send_alert(client_id, device_id, device, data):
    try:
        print("///////////////////////////////////////////////////////////")
        print(data)
        logging.error(data)
    except Exception as e:
        print(e)
        logging.error(e)