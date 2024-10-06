import RPi.GPIO as GPIO
import accelerometer

deploypin = 26
GPIO.setmode(GPIO.board)
GPIO.setup(deploypin, GPIO.OUT)

while True:
  ACC = accelerometer.read(10)
  if ACC < 0,8:
  GPIO.setup(deploypin, GPIO.HIGH)

  