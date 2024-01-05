import pika, os

rabbitmq_url = 'amqps://agulscpl:wYEC0zMsYf67l_Hr7wQavMcvHBA6Y0RI@hawk.rmq.cloudamqp.com/agulscpl'
url = os.environ.get('RABBITMQ_URL', rabbitmq_url)
#url = os.environ.get('RABBITMQ_URL', 'amqp://guest:guest@localhost:5672/')
params = pika.URLParameters(url)
connection = pika.BlockingConnection(params)
channel = connection.channel()

channel.exchange_declare('test_exchange')
channel.queue_declare(queue='test_queue')
channel.queue_bind('test_queue', 'test_exchange', 'tests')

#publish message
channel.basic_publish(
    body="Hello Mati!",
    exchange='test_exchange',
    routing_key='tests'
   )
print('Message sent.')
channel.close()
connection.close()
