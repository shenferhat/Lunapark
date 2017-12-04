import sys
from aesencryption import AESCipher
import konfig
import paho.mqtt.publish as publish

def main(args):
    return 0
	
if __name__ == '__main__':
    encrypter = AESCipher(konfig.AESPassword)
    encryptedData = encrypter.encrypt("SELECT uahsdkjashkjdaksjhdkjashdkjhaskhdkasdksjkghkjfdhjgkhdfkjgkjhdfhdsljsdkjflksdfkljsdklj ")
    publish.single(konfig.subscribeChannel, encryptedData, hostname=konfig.mqttServerAddress)
