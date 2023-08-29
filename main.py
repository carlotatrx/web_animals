import asyncio

import tornado.web

print("Hello, docker!")

class MainHandler(tornado.web.RequestHandler):
    def get(self):
        print("Helloooooo TORNADO 3***")
        self.write("Hello, world")

def make_app():
    return tornado.web.Application([
        (r"/", MainHandler),
    ])

async def main():
    app = make_app()
    app.listen(8888)
    await asyncio.Event().wait()

if __name__ == "__main__":
    asyncio.run(main())
