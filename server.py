import asyncio
import threading
from aiohttp import web
from routes import setup_routes
import aiohttp_jinja2
import jinja2

PORT = 8080
HOST = '0.0.0.0'

def aiohttp_server():
  app = web.Application()
  setup_routes(app)
  app.add_routes([web.static('/static', 'static')])
  aiohttp_jinja2.setup(app,loader=jinja2.FileSystemLoader('templates'))

  runner = web.AppRunner(app)
  return runner

def run_server(runner):
  loop = asyncio.new_event_loop()
  asyncio.set_event_loop(loop)
  loop.run_until_complete(runner.setup())
  site = web.TCPSite(runner, HOST, PORT)
  loop.run_until_complete(site.start())
  loop.run_forever()

def run():
  t = threading.Thread(target=run_server, args=(aiohttp_server(),))
  t.start()
  print('SERVER: Online at http://' + HOST + ':' + str(PORT))