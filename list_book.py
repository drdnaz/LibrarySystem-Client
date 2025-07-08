import paho.mqtt.client as mqtt
import time
from dotenv import load_dotenv
import os

load_dotenv()
BROKER = os.getenv("BROKER")
PORT = int(os.getenv("PORT"))
TOPIC_ALL = "naz/book/list-all"
TOPIC_ONE = "naz/book/list"

def publish_list_all():
    client = mqtt.Client()
    client.connect(BROKER, PORT, 60)
    client.loop_start()

    client.publish(TOPIC_ALL, "")
    print("List all books message sent.")

    time.sleep(1)
    client.loop_stop()

def publish_list_one(id_str):
    client = mqtt.Client()
    client.connect(BROKER, PORT, 60)
    client.loop_start()

    client.publish(TOPIC_ONE, id_str)
    print(f"List book by ID message sent: id={id_str}")

    time.sleep(1)
    client.loop_stop()

if __name__ == "__main__":
    publish_list_all()
    publish_list_one("2")
