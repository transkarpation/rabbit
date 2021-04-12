import pika
import sys
import ConnectLocal

bind_simple = True

if len(sys.argv) > 1:
    bind_simple = False

channel = ConnectLocal.do_connect()

if bind_simple:
    channel.queue_declare('simple_bind')
    print('implicit binding is done --> check the managment UI')
else:
    channel.queue_declare('direct_bind')
    channel.queue_bind(queue = "direct_bind", exchange="amq.direct", routing_key="demonstrate")
    print("bound queue 'direct_bind' to exchange 'amq.direct' with key 'demonstarte'")
channel.close()