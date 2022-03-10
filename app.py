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
GPIO.setup(19, GPIO.IN, pull_up_down=GPIO.PUD_UP)
while True:
  input_state = GPIO.input(19)
  if input_state == False:
    print('Button Pressed')
    sleep(0.2)