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
  global lastDisplayed, todoList
  print('updating...')
  if todoList == lastDisplayed: return
  print('changes found')
  display.showItems(todoList)
  print('updated thread')
  lastDisplayed = copy.deepcopy(todoList)

# Import server from server file
import server
import display

set_interval(updateDisplay, 5)
updateDisplay()
server.run()