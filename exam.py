import pika, ssl

url = 'amqps://student:XYR4yqc.cxh4zug6vje@rabbitmq-exam.rmq3.cloudamqp.com/mxifnklj'
params = pika.URLParameters(url)
connection = pika.BlockingConnection(params)
channel = connection.channel()

try:
    # Declare the exchange
    exchange_name = "exchange.611fc7d4-c020-449c-8582-7d8da065af65"
    channel.exchange_declare(exchange=exchange_name, exchange_type='direct', durable=True)

    # Declare the queue
    queue_name = "exam"
    channel.queue_declare(queue=queue_name, durable=True)

    # Bind the queue to the exchange with the specified routing key
    routing_key = "611fc7d4-c020-449c-8582-7d8da065af65"
    channel.queue_bind(exchange=exchange_name, queue=queue_name, routing_key=routing_key)

    # Define the message payload
    message_body = "Hi CloudAMQP, this was fun!"

    # Publish the persistent message to the queue with the specified routing key
    channel.basic_publish(
        exchange=exchange_name,
        routing_key=routing_key,
        body=message_body,
        properties=pika.BasicProperties(
            delivery_mode=2,  # Make the message persistent
        )
    )

finally:
    channel.exchange_delete(exchange=exchange_name)
    connection.close()