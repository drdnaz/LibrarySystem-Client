import paho.mqtt.client as mqtt
import time
from dotenv import load_dotenv
import os

load_dotenv()
BROKER = os.getenv("BROKER")
PORT = int(os.getenv("PORT"))
TOPIC = "naz/kutuphane/sil"

def publish_delete_kutuphane(kutuphane_id: str):
    client = mqtt.Client()
    client.connect(BROKER, PORT, 60)
    client.loop_start()

    client.publish(TOPIC, kutuphane_id)
    print(f"Kütüphane silme mesajı gönderildi: {kutuphane_id}")

    time.sleep(1)
    client.loop_stop()

if __name__ == "__main__":
    publish_delete_kutuphane("")
