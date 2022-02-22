from time import sleep
import logging
import server

# Todo list storage
todoList = []

# Remove flask logs
import logging
flaskLogger = logging.getLogger('werkzeug')
flaskLogger.setLevel(logging.ERROR)

while True:
  print(todoList)
  sleep(2)