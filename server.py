from flask import Flask, render_template, request
from flask_assets import Bundle, Environment
import __main__
import threading

server = Flask(__name__)
assets = Environment(server)

css = Bundle('src/main.css', output='dist/main.css', filters='postcss', depends=('templates/index.html'))
assets.register('main_css', css)
css.build()
 
@server.route("/")
def index():
  return render_template("index.html", list=__main__.todoList, len=len(__main__.todoList))

@server.route("/items")
def items():
  return {"items": __main__.todoList}

@server.route("/syncitems", methods=['POST'])
def sync():
  body = request.json
  if body == None or not isinstance(body, list):
    return 'Invalid body', 400
  
  for item in body:
    if not "name" in item or not "completed" in item:
      return 'Invalid items', 400
  
  if len(body) > 50:
    return 'Too many items', 400

  __main__.todoList = body
  return {"items": __main__.todoList}

# Run flask server
threading.Thread(target=lambda: server.run(host="0.0.0.0", port="2000", debug=True, use_reloader=False)).start()
