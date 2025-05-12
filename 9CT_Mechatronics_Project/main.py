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

#Settings
detect_distance = 150 #150mm
check_block_distance = 5 #5mm

#Start

#block finding and moving
while True:
    #finding block
    counter = 60
    found_block = False
    while counter > 0 and found_block == False:
        ev3.screen.print(counter)
        if ultrasonic_sensor.distance() < detect_distance:
            found_block = True
            ev3.screen.print("Block found")

        counter -= 1
        robot.turn(3)
        ev3.screen.clear()

    if found_block:
        #go to block
        found_block = False
        while ultrasonic_sensor.distance() > check_block_distance:
            ev3.screen.print(ultrasonic_sensor.distance())
            robot.straight(5) #move forward 5mm
            ev3.screen.clear()
    
        #check block colour
        current_color = colour_sensor.color()
        ev3.screen.print(current_color)

        if current_color == Color.RED or Color.YELLOW:
            ev3.screen.print("Good block found")
            ev3.screen.print(current_color)
            ev3.screen.clear()
            #take block back to the start\

    wait(10)
    ev3.screen.clear()

#end
ev3.screen.print("Finished")