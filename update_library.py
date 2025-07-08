import paho.mqtt.client as mqtt
import time
from dotenv import load_dotenv
import os

load_dotenv()
BROKER = os.getenv("BROKER")
PORT = int(os.getenv("PORT"))
TOPIC = "naz/library/update"

def publish_update_library(message: str):
    client = mqtt.Client()
    client.connect(BROKER, PORT, 60)
    client.loop_start()

    client.publish(TOPIC, message)
    print(f"Library update message sent: {message}")

    time.sleep(1)
    client.loop_stop()

if __name__ == "__main__":
    publish_update_library("1,Science Fiction")
