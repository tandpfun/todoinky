from aiohttp import web
import aiohttp_jinja2
import __main__

@aiohttp_jinja2.template('index.html')
async def index(request):
  return {"a": "b"}

async def items(request):
  return web.json_response({"items": __main__.todoList})

async def sync(request):
  body = await request.json()
  if body == None or not isinstance(body, list):
    return web.Response(text='Invalid body', status=400)
  
  for item in body:
    if not "name" in item or not "completed" in item:
      return web.Response(text='Invalid items', status=400)
  
  if len(body) > 50:
    return web.Response(text='Too many items', status=400)

  __main__.todoList = body
  return web.json_response({"items": __main__.todoList})