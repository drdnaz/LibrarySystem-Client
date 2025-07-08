import time
import paho.mqtt.client as mqtt
from dotenv import load_dotenv
import os

load_dotenv()
BROKER = os.getenv("BROKER")
PORT = int(os.getenv("PORT"))

def publish_create_library(message: str):
    TOPIC = "naz/library/create"
    client = mqtt.Client()
    client.connect(BROKER, PORT, 60)
    client.loop_start()

    client.publish(TOPIC, message)
    print(f"Library creation message sent: {message}")

    time.sleep(1)
    client.loop_stop()

if __name__ == "__main__":
    # publish_create_library("Novels")

    publish_create_library("Korkutata Library")
