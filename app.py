from threading import Thread, Timer
from time import sleep
import RPi.GPIO as GPIO

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

# Import server from server file
import server
import display

Thread(target=display.start).start()
server.run()

# Buttons
GPIO.setmode(GPIO.BCM)
GPIO.setup(23, GPIO.IN, pull_up_down=GPIO.PUD_UP)

def handleButtonPress(index):
  print(todoList[index]['completed'])
  print(index)
  if todoList[index]['completed'] == True:
    todoList[index]['completed'] = False
  else:
    todoList[index]['completed'] = True

  print(todoList[index]['completed'])

currentPressState = False
while True:
  input_state = GPIO.input(23)
  if input_state == False and currentPressState == False:
    currentPressState = True
    handleButtonPress(0)
    print('pressed')
  
  if input_state == True:
    currentPressState = False
  
  sleep(0.01)