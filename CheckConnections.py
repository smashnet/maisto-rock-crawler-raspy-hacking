try:
      import RPi.GPIO as GPIO
      import time
except RuntimeError:
      print("Error importing RPi.GPIO!  This is probably because you need superuser privileges.  You can achieve this by using 'sudo' to run your script")

STEER_LEFT = 17
STEER_RIGHT = 18
DRIVE_FORWARD = 23
DRIVE_BACKWARD = 24

def initGPIO():
  GPIO.setmode(GPIO.BCM)

  GPIO.setup(STEER_LEFT, GPIO.OUT, initial=GPIO.LOW)
  GPIO.setup(STEER_RIGHT, GPIO.OUT, initial=GPIO.LOW)
  GPIO.setup(DRIVE_FORWARD, GPIO.OUT, initial=GPIO.LOW)
  GPIO.setup(DRIVE_BACKWARD, GPIO.OUT, initial=GPIO.LOW)

def resetMotors():
  #Set everything to zero
  GPIO.output(STEER_LEFT, GPIO.LOW)
  GPIO.output(STEER_RIGHT, GPIO.LOW)
  GPIO.output(DRIVE_FORWARD, GPIO.LOW)
  GPIO.output(DRIVE_BACKWARD, GPIO.LOW)

def doTesting():
  print "Reset everything"
  resetMotors()
  time.sleep(0.5)
  GPIO.output(STEER_LEFT, GPIO.HIGH)
  print "Steer left"
  time.sleep(1)
  GPIO.output(STEER_LEFT, GPIO.LOW)
  GPIO.output(STEER_RIGHT, GPIO.HIGH)
  print "Steer right"
  time.sleep(1)
  GPIO.output(STEER_RIGHT, GPIO.LOW)
  GPIO.output(DRIVE_FORWARD, GPIO.HIGH)
  print "Drive forwards"
  time.sleep(0.5)
  GPIO.output(DRIVE_FORWARD, GPIO.LOW)
  GPIO.output(DRIVE_BACKWARD, GPIO.HIGH)
  print "Drive backwards"
  time.sleep(0.5)
  GPIO.output(DRIVE_BACKWARD, GPIO.LOW)

  

initGPIO()
print "Starting Rover test..."
doTesting()

GPIO.cleanup()
print "Test finished :-)"
