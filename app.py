from threading import Thread

# Todo list storage
global todoList
todoList = [
  {
    "name": "Go to school",
    "completed": True,
  }
]

def updateDisplay():
  Thread(target=display.showItems, args=(todoList,)).start()

# Import server from server file
import server
import display

updateDisplay()
server.run()