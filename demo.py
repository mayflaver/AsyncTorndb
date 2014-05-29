import tornado.ioloop
import tornado.web
import connections
import tornado.gen

class MainHandler(tornado.web.RequestHandler):
    @tornado.gen.coroutine
    def get(self):
        conn = connections.Connection(user='root', passwd='toor', database='dev_server')
        yield conn.connect()
        data = yield conn.get('select * from test where id=%s limit 0, 1', 1)
        print(data)
        self.write("Hello, world")

application = tornado.web.Application([
    (r"/", MainHandler),
])

if __name__ == "__main__":
    application.listen(8888)
    tornado.ioloop.IOLoop.instance().start()
