#!/usr/bin/env pybricks-micropython
from pybricks.hubs import EV3Brick
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor,
                                 InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.parameters import Port, Stop, Direction, Button, Color
from pybricks.tools import wait, StopWatch, DataLog
from pybricks.robotics import DriveBase
from pybricks.media.ev3dev import SoundFile, ImageFile

sensor_motor = Motor(Port.A)
colour_sensor = ColorSensor(Port.S3)
ev3 = EV3Brick()
left_motor = Motor(Port.B)
right_motor = Motor(Port.C)
robot = DriveBase(left_motor, right_motor, wheel_diameter=55.5, axle_track=104)
colour_sensor = ColorSensor(Port.S3)
ultrasonic_sensor = UltrasonicSensor(Port.S2)
BLACK = 9
WHITE = 85
threshold = (BLACK + WHITE) / 2
block_grabbed = False
block_found = False
detect_distance = 500
check_block_distance = 80
current_color = colour_sensor.color()
block_counter = 0

def block_search():
   global block_found
   if block_grabbed == False and block_found == False:
       while block_found == False:
          counter1 = 30
          counter2 = 60
          while counter1 > 0:
            counter1 -= 1
            robot.turn(3)
            ev3.screen.print(ultrasonic_sensor.distance())
            if ultrasonic_sensor.distance() < detect_distance:
               block_found = True
               break
          while counter2 > 0:
            counter2 -= 1
            robot.turn(-3)
            ev3.screen.print(ultrasonic_sensor.distance())
            if ultrasonic_sensor.distance() < detect_distance:
               block_found = True
               break
    
          robot.turn(30)
          robot.straight(10)


def block_check():
    global block_grabbed
    global block_found
    if block_found == True and block_grabbed == False:
        while ultrasonic_sensor.distance() > check_block_distance:
           robot.straight(2.5)
    if current_color == Color.RED or Color.YELLOW:
        wait(30)
        robot.straight(2.5)
        sensor_motor.run_angle (90,90)
        block_found = False
        block_grabbed = True
    else:
        ev3.screen.print("Bad block found")
        ev3.screen.print(current_color)
        ev3.screen.clear()
        robot.straight(-10)
        robot.turn(-90)
        robot.straight(10)
        robot.turn(90)
        robot.straight(20)
        robot.turn(10)
        robot.straight(10)
        robot.turn(-90)
        sensor_motor.run_angle (90,90)
        block_found = False
def block_return():
  global block_grabbed 
  colour_sensor_reflection = colour_sensor.reflection()
  while colour_sensor_reflection > 60:
    deviation = colour_sensor.reflection() - threshold
    turn_rate = 1.2 * deviation
    robot.drive(10, turn_rate)
    wait(10)
    colour_sensor_reflection = colour_sensor_reflection()
  robot.straight(-10)
  robot.turn(90)
  block_grabbed = False
  block_counter =+ 1

# Main Loop
while True:
    block_search()
    block_check()
    block_return()
    if block_counter == 2:
       break