# Todo list storage
global todoList
todoList = [
  {
    "name": "Go to sleep",
    "completed": False
  }
]

from time import sleep
import logging
import server

server.run()