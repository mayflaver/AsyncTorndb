AsyncTorndb(inactive)
=====================

Async mysql client for tornado base on [PyMySQL](https://github.com/PyMySQL/PyMySQL).

Documentation
===========

AsyncTorndb behavior is almost like torndb behavior, but async. Refer to [torndb](http://torndb.readthedocs.org)
and have a try.

Requirements
===========

 * [tornado](https://github.com/tornadoweb/tornado) with latest

Demo
===========

Here is a simple "Hello, world" example web app for AsyncTorndb::

    import tornado.ioloop
    import tornado.web
    import tornado.gen
    import asynctorndb
    
    class MainHandler(tornado.web.RequestHandler):
        @tornado.gen.coroutine
        def get(self):
            conn = asynctorndb.Connect(user='demo', passwd='demo', database='demo')
            yield conn.connect()
            result = yield conn.query('select * from user')
            # do something with result
            self.write("Hello, world")

    application = tornado.web.Application([
        (r"/", MainHandler),
    ])

    if __name__ == "__main__":
        application.listen(8888)
        tornado.ioloop.IOLoop.instance().start()

License
===========

AsyncTorndb is released under the MIT License. See LICENSE for more information.
