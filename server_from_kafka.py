from kafka import KafkaConsumer
import sys
import json
import time

consumer = KafkaConsumer(
    'final_project',
     bootstrap_servers=['localhost:9092'],
     auto_offset_reset='earliest',
     enable_auto_commit=True,
     group_id='my-group-' + str(time.time()),
     value_deserializer=lambda x: x.decode('utf-8'))

kafka_data = []
for message in consumer:
 kafka_data.append(message[6])
 print(message[6])

sys.exit()

