import paho.mqtt.client as mqtt
import time
from dotenv import load_dotenv
import os

load_dotenv()
BROKER = os.getenv("BROKER")
PORT = int(os.getenv("PORT"))
TOPIC = "naz/book/create"

def publish_create(message: str):
    client = mqtt.Client()
    client.connect(BROKER, PORT, 60)
    client.loop_start()

    client.publish(TOPIC, message)
    print(f"Book creation message sent: {message}")

    time.sleep(1)
    client.loop_stop()

if __name__ == "__main__":
    publish_create("Madonna in a Fur Coat,Sabahattin Ali,160,YKY")
