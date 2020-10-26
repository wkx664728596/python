
import pika
import json

credentials = pika.PlainCredentials(username='wkx',password='wkx')
parameters = pika.ConnectionParameters(host='47.104.193.180',port=5672,virtual_host='OZ_JS',credentials=credentials)
connection = pika.BlockingConnection(parameters)
channel = connection.channel()

# 创建队列
channel.queue_declare(queue='test')

# 向队列插入数据
channel.basic_publish(exchange='',
                      routing_key = 'test',
                      body = json.dumps({'name':'wkx','phone':'15994092160'}))

print('producer queue')

connection.close()
