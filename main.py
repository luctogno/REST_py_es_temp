import sys
import urllib2
from datetime import datetime
from elasticsearch import Elasticsearch
import time
import random
import datetime

es_ip="192.168.0.25"
es_port=9200

timeout_in_minutes=1

es = Elasticsearch(hosts=[{'host': es_ip, 'port': es_port}],)

es_index = "temperature_monitor_test"
es_type = "temp_entry"

arduino_ip="192.168.0.205"
arduino_port=80

def randomTemp():
        return random.uniform(16.2, 22.3)

def get_json_from_arduino(ip, port, path):
	return urllib2.urlopen(ip+":"+str(port)+"/" + path).read()
	
def send_data_to_es(index, type, message):
	es.index(index=index, doc_type=type, body=message)
	
def loop():
	print("Do Stuff")
	#temp_data = get_json_from_arduino(arduino_ip, arduino_port, path)
	#temp_data = get_json_from_arduino("http://ip.jsontest.com", 80, "/posts/1")
        temp_data = "{{\"temperature\":"+randomTemp()+", \"author\": \"testPI\", \"ttimestamp\": "+str(int(datetime.datetime.now().strftime("%s")))"}"
	print temp_data
	send_data_to_es(es_index, es_type, temp_data)
	
def main():
	print("Hi")
	try:
            while True:
                loop()
                time.sleep(timeout_in_minutes*60)
	except:
                print "fuck"
                raise

if __name__ == "__main__":
	# execute only if run as a script
	main()
