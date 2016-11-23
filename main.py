import sys
import http.client, urllib.parse
from datetime import datetime
from elasticsearch import Elasticsearch
from interruptingcow import timeout

es_ip="192.168.0.25"
es_port=9200

timeout_in_minutes=1

es = Elasticsearch(hosts=[{'host': es_ip, 'port': es_port}],)

es_index = "temperature_monitor"
es_type = "temp_entry"

arduino_ip="192.168.0.205"
arduino_port=80

def get_json_from_arduino(ip, port, path):
	conn = http.client.HTTPSConnection(ip, port)
	conn.request("GET", path)
	
def send_data_to_es(index, type, message):
	es.index(index=index, doc_type=type, body=message)
	
def loop():
	print("Do Stuff")
	temp_data = get_json_from_arduino(arduino_ip, arduino_port)
	send_data_to_es(es_index, es_type, temp_data)
	
def main():
	print("Hi")
	try:
		with timeout(60*timeout_in_minutes, exception=RuntimeException):
			while true:
				loop()
				print("Waiting")
	except RuntimeException:
		pass

if __name__ == "__main__":
	# execute only if run as a script
	main()