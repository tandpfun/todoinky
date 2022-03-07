# Todo list storage
global todoList
todoList = [
  {
    "name": "Go to school",
    "completed": True,
  }
]

def updateDisplay():
  display.showItems(todoList)

# Import server from server file
import server
import display

server.run()
updateDisplay()