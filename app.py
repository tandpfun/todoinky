from threading import Thread, Timer
import copy
from turtle import update

# Todo list storage
global todoList
todoList = [
  {
    "name": "Go to school",
    "completed": True,
  }
]

def set_interval(func, sec):
  def func_wrapper():
    set_interval(func, sec)
    func()
  t = Timer(sec, func_wrapper)
  t.start()
  return t

lastDisplayed = []
def updateDisplay():
  global lastDisplayed
  print(lastDisplayed)
  if todoList == lastDisplayed: return
  lastDisplayed = copy.deepcopy(todoList)
  Thread(target=display.showItems, args=(todoList,)).start()

# Import server from server file
import server
import display

set_interval(updateDisplay, 4)
updateDisplay()
server.run()