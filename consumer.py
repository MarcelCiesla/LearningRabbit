import pika, os

rabbitmq_url = 'amqps://agulscpl:wYEC0zMsYf67l_Hr7wQavMcvHBA6Y0RI@hawk.rmq.cloudamqp.com/agulscpl'
url = os.environ.get('RABBITMQ_URL', rabbitmq_url)
#url = os.environ.get('RABBITMQ_URL', 'amqp://guest:guest@localhost:5672/')
params = pika.URLParameters(url)
connection = pika.BlockingConnection(params)
channel = connection.channel()
channel.queue_declare(queue='test_queue')

def callback(ch, method, properties, body):
    print(' [x] Received ' + str(body))

channel.basic_consume(
    'test_queue',
    callback,
    auto_ack=True) 

print(' [*] Waiting for messages:')
channel.start_consuming()
connection.close()