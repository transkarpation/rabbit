import pika
import ConnectLocal as conn

with conn.do_connect() as channel:
    queue_ok_result = channel.queue_declare("pika_queue", passive=True)
    print(queue_ok_result.method)