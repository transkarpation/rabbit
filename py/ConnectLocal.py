import pika

def do_connect():
    creds = pika.PlainCredentials("guest", "guest")
    conn_param = pika.connection.ConnectionParameters(credentials=creds)
    connection = pika.BlockingConnection(conn_param)
    channel = connection.channel()
    return channel
