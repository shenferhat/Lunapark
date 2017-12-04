import sys
import paho.mqtt.publish as publish
import paho.mqtt.client as mqtt
from aesencryption import AESCipher
import konfig
from postgresql import PostgreSQL

def on_connect(client, userdata, flags, rc):
	print("Connected with result code "+str(rc))

def on_message(client, userdata, msg):
	print "Message"
	print(msg.topic+"\nAES Message:"+str(msg.payload))
	encryptedData = msg.payload
	db = PostgreSQL();
	encryptor = AESCipher(konfig.AESPassword)
	decryptedData = encryptor.decrypt(encryptedData)
	if "select" in decryptedData.lower():
		print "Sorgu:"+decryptedData+"\n"
		#print db.executeQuery(decryptedData)

if __name__ == "__main__":
	client = mqtt.Client()
	client.on_connect = on_connect
	client.on_message = on_message
	client.connect(konfig.mqttServerAddress, konfig.mqttServerPort, 60)
	client.subscribe(konfig.subscribeChannel,0)
	client.loop_forever()
	
