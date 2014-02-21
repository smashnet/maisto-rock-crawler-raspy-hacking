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
  GPIO.setwarnings(False)
  GPIO.setmode(GPIO.BCM)

  GPIO.setup(STEER_LEFT, GPIO.OUT, initial=GPIO.LOW)
  GPIO.setup(STEER_RIGHT, GPIO.OUT, initial=GPIO.LOW)
  GPIO.setup(DRIVE_FORWARD, GPIO.OUT, initial=GPIO.LOW)
  GPIO.setup(DRIVE_BACKWARD, GPIO.OUT, initial=GPIO.LOW)

def cleanupGPIO():
  GPIO.cleanup()

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
  time.sleep(0.2)
  GPIO.output(DRIVE_FORWARD, GPIO.LOW)
  time.sleep(0.5)
  GPIO.output(DRIVE_BACKWARD, GPIO.HIGH)
  print "Drive backwards"
  time.sleep(0.2)
  GPIO.output(DRIVE_BACKWARD, GPIO.LOW)

def steerStraight():
  try:
    GPIO.output(STEER_RIGHT, GPIO.LOW)
    GPIO.output(STEER_LEFT, GPIO.LOW)
  except:
    return 1
  return 0

def steerLeft():
  try:
    GPIO.output(STEER_RIGHT, GPIO.LOW)
    GPIO.output(STEER_LEFT, GPIO.HIGH)
  except:
    return 1
  return 0

def steerRight():
  try:
    GPIO.output(STEER_LEFT, GPIO.LOW)
    GPIO.output(STEER_RIGHT, GPIO.HIGH)
  except:
    return 1
  return 0

def driveStop():
  try:
    GPIO.output(DRIVE_BACKWARD, GPIO.LOW)
    GPIO.output(DRIVE_FORWARD, GPIO.LOW)
  except:
    return 1
  return 0

def driveForward():
  try:
    GPIO.output(DRIVE_BACKWARD, GPIO.LOW)
    GPIO.output(DRIVE_FORWARD, GPIO.HIGH)
  except:
    return 1
  return 0

def driveBackward():
  try:
    GPIO.output(DRIVE_FORWARD, GPIO.LOW)
    GPIO.output(DRIVE_BACKWARD, GPIO.HIGH)
  except:
    return 1
  return 0
