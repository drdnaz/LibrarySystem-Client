import paho.mqtt.client as mqtt
import time
from dotenv import load_dotenv
import os

load_dotenv()
BROKER = os.getenv("BROKER")
PORT = int(os.getenv("PORT"))
TOPIC = "naz/kutuphane/kitap-ekle"

def publish_add_kitap(payload: str):
    client = mqtt.Client()
    client.connect(BROKER, PORT, 60)
    client.loop_start()

    client.publish(TOPIC, payload)
    print(f"Kütüphaneye kitap ekleme mesajı gönderildi: {payload}")

    time.sleep(1)
    client.loop_stop()

if __name__ == "__main__":
    publish_add_kitap("1")  # Örnek: kutuphane_id=1, kitap_id=2
