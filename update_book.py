import paho.mqtt.client as mqtt
import time
from dotenv import load_dotenv
import os

load_dotenv()
BROKER = os.getenv("BROKER")
PORT = int(os.getenv("PORT"))
TOPIC = "naz/kitap/degis"

def publish_update(message: str):
    client = mqtt.Client()
    client.connect(BROKER, PORT, 60)
    client.loop_start()

    client.publish(TOPIC, message)
    print(f"Kitap güncelleme mesajı gönderildi: {message}")

    time.sleep(1)
    client.loop_stop()

if __name__ == "__main__":
    # Örnek kullanım (id,isim,yazar,sayfa,yayinci):
    publish_update("1,İnce Memed,Yaşar Kemal,430,YKY")
