import tornado.ioloop
import tornado.web
import os.path
import imp
from subprocess import Popen, PIPE, STDOUT,call


class IndexHandler(tornado.web.RequestHandler):
    def get(self):
        self.render("index.html")


class WebSocketHandler(tornado.web.RequestHandler):
    def get(self):
        if os.path.exists('/home/samara/Documentos/TG/TG-Background/Code/run_finger.py'):
            p = Popen(["python","/home/samara/Documentos/TG/TG-Background/Code/run_finger.py"], stdout=PIPE).communicate()[0] 
            self.write(p)
    def on_message(self, message):
        self.write_message(u"Servidor repete: " + message)

def web_app():
    return tornado.web.Application([
        (r"/", IndexHandler),
        (r"/websocket", WebSocketHandler),
    ])

if __name__ == "__main__":
    app = web_app()
    app.listen(8768)
    tornado.ioloop.IOLoop.current().start()