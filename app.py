# Todo list storage
global todoList
todoList = [
  {
    "name": "Go to school",
    "completed": True,
  }
]

# Import server from server file
import server
import display

server.run()
display.showItems(todoList)