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
buttons = {
  0: 0,
  1: 1,
  5: 2,
  23: 3,
  24: 4
}

GPIO.setmode(GPIO.BCM)

for pin in buttons.keys():
  GPIO.setup(pin, GPIO.IN, pull_up_down=GPIO.PUD_UP)

def handleButtonPress(pin):
  if not pin in buttons:
    return print('[!] Button not in pins')
  
  index = buttons[pin]

  if len(todoList) - 1 < index:
    return print('[!] No item for the button pressed')

  if todoList[index]['completed'] == True:
    todoList[index]['completed'] = False
  else:
    todoList[index]['completed'] = True

currentPressState = False
while True:
  for pin in buttons.keys():
    input_state = GPIO.input(pin)
    if input_state == False and currentPressState == False:
      currentPressState = True
      handleButtonPress(pin)
      print('Pressed pin ' + str(pin))

    if input_state == True:
      currentPressState = False
  
  sleep(0.01)