import asyncio
import threading
from aiohttp import web
from routes import setup_routes

HOST = '0.0.0.0'
PORT = 8080

def aiohttp_server():
  app = web.Application()
  setup_routes(app)
  app.add_routes([web.static('/static', 'static')])

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
  threading.Thread(target=run_server, args=(aiohttp_server(),)).start()
  print()
  print('[SERVER] Listening for requests at http://' + HOST + ':' + str(PORT))