import tornado
from tornado.websocket import WebSocketHandler as WS

clients = []

class WebSocketHandler(WS):
    def check_origin(self, origin):
        print ("origin: " + origin)
        return True
    # the client connected
    def open(self):
        print ("New client connected")
        self.write_message("You are connected")
        clients.append(self)

    # the client sent the message
    def on_message(self, message):
        print ("message: " + message)
        self.write_message(message)

    # client disconnected
    def on_close(self):
        print ("Client disconnected")
        clients.remove(self)
