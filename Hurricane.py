import subprocess, sys
from datetime import timedelta
pybin = sys.executable#
try: # tornado
	import tornado
	print("tornado available")
except ImportError:
	subprocess.check_call([pybin, '-m', 'pip', 'install', 'tornado'])
	import tornado
	print("tornado installed")
	
from Backend.Greeting import Basic
from Backend.Clients import WebSocketHandler, clients

def send_message_to_clients():
	try:
		# read_my_data()
		for client in clients:
			client.write_message({time:datetime()})
			pass# Do whatever
	finally:
		tornado.ioloop.IOLoop.instance().add_timeout(timedelta(seconds=3), send_message_to_clients)

socket = tornado.web.Application([
	(r"/ws", WebSocketHandler),
	(r"/", Basic), ])

if __name__ == "__main__":
	host, port = 'localhost', 8888
	socket.listen(port,host)
	print(f'http://{host}:{port}')
	tornado.ioloop.IOLoop.instance().add_timeout(timedelta(seconds=3), send_message_to_clients)
	tornado.ioloop.IOLoop.instance().start()

# RUN
# python3 Hurricane.py
