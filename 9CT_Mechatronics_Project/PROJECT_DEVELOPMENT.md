# **9CT Assessment Task 1**
### By Oscar Dodd

## **Requirements outline**
### The purpose
- I need to design a robot that can detect and move different coloured blocks using its sensors. It needs to take the correct coloured blocks to the start.

### Key actions
- Rotate 90 degrees then move forward by 5cm
- Rotate slowly until block detected by ultrasonic sensor.
- Move forward until ultrasonic sensor detects that the block is within 1cm.
- check the colour of the block using the colour sensor.
- if the colour is not red or yellow then move around it, if it is red or yellow, take it back to the start.

### Functional requirements
- Block detection - the robot will move slowly up to the block until the colour sensor can detect its colour.
- Block classification - the robot will check the blocks colour and if it is red or yellow then it will move it to the start.
- Block avoidance - if the block is not red or yellow then it will move back by 5cm, turn left by 90 degrees and move forward by 5cm.
- Block movement - if the block is red or yellow it will pick it up by a mechanism and take it to the start.

### Use cases
1. Block detection
    - Scenario: The robot is moving around and detects a block
    - Inputs: The ultrasonic sensor detects something within 30cm
    - Action: The robot slowly moves towards it until the block is within 1cm
    - Expected Outcome: The robot moves up to a block
2. Block classification
    - Scenario: The robot detects and moves up to a block
    - Inputs: The colour sensor detects a colour infront
    - Action: The robot will check if the colour is red or yellow
    - Expected Outcome: The robot will do an action based on the colour of the block 
3. Block avoidance
    - Scenario: The colour sensor has deetected that the block infront of the robot is not red or yellow
    - Inputs: The colour sensor detects a colour that isnt red or yellow
    - Action: The robot will move back by 5cm then turn left by 90 degrees then move forward by 5cm
    - Expected Outcome: The robot avoids and goes around the incorrect coloured block 
4. Block movement
    - Scenario: The colour sensor has detected that the block infront of the robot is red or yellow
    - Inputs: The colour sensor detects a colour that is red or yellow
    - Action: The robot will use a mechanism to grab the block infront and take it back to the start
    - Expected Outcome: The robot will move the correct colour block to the start

### Test cases
| Test Case | Input     | Expected Output   |
|---------- |---------- |----------------   |
|red/yellow block|Colour sensor finds a red/yellow block|The robot will use a mechanism to take the block to the start|
|non red/yellow block|Colour sensor finds a non red/yellow block|The robot will move back by 5cm, turn left by 90 degrees, and move forward by 5cm|
|block found|The ultrasonic sensor finds a block near infront of the robot|The robot will move forward until the ultrasonic sensor detects that the block is within 1cm|
|avoiding leaving the designated area|The colour sensor detects the colour black|The robot will move rotate until it no longer detects black|

### Non-functional requirements
- Efficiency: the robot should do actions fast and without error.
- Response Time: the robot should react to a sensor input within 1 second.
- Accuracy: The robot should be able to do most actions without any errors or mistakes

## **Design**
### Algoriths and pseudocode
#### Algorithm 1 Flowchart
![alt text](<Screenshot 2025-05-17 at 9.05.37 pm.png>)
#### Algorithm 1 Pseudocode
```python
BEGIN
    WHILE true
        block_search
        block_check
        block_return
        IF block_counter == 2
            BREAK
    ENDWHILE
END
```

#### Algorithm 2 Flowchart
![alt text](<Screenshot 2025-05-17 at 10.18.25 pm.png>)
#### Algorithm 2 Pseudocode
```python
BEGIN block_search
    IF block_grabbed == false AND block_found == false
        WHILE block_found == false
            counter1 = 30
            counter2 = 60
            WHILE counter1 > 0
                counter1 - 1
                Turn right by 3 degrees
                Print on the screen the ultrasonicsensor distance
                IF ultrasonic sensor distance < detect_distance
                    block_found = true
                    BREAK
            ENDWHILE
            WHILE counter2 > 0
                counter2 - 1
                Turn left by 3 degrees
                Print on the screen the ultrasonicsensor distance
                IF ultrasonic sensor distance < detect_distance
                    block_found = true
                    BREAK
            ENDWHILE
        ENDWHILE
END block_search
```

#### Algorithm 3 FLowchart
![alt text](<Screenshot 2025-05-18 at 6.36.19 pm.png>)
#### Algorithm 3 Pseudocode
```python
BEGIN block_check
    IF block_found == true and block_grabbed == false
        WHILE ultrasonic sensor distance > check_block_distance
            Move forward
        ENDWHILE
    IF current_color == red or yellow
        Wait 3 seconds
        Rotate colour sensor
        block_found = false
        block_grabbed = true
    ELSE
        Print bad block found
        Print the current colour
        Wait 3 seconds
        Clear the screen
        Go around the block
        Rotate colour sensor
        block_found = false
END block_check
```

## **Development and Integration**

#### The test program used to test the movement of the sensor movement mechanism's various iterations.
```python
 #!/usr/bin/env pybricks-micropython
from pybricks.hubs import EV3Brick
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor,
                                 InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.parameters import Port, Stop, Direction, Button, Color
from pybricks.tools import wait, StopWatch, DataLog
from pybricks.robotics import DriveBase
from pybricks.media.ev3dev import SoundFile, ImageFile

sensor_motor = Motor(Port.A)

"""Used to test the movement of the colour sensor's motor, using run_angle to move the motor at 
a speed of 90 degrees per second for 90 degrees, to stop the motor from hitting the ground or the wheels.
It then moves it back to it's previous position."""

sensor_motor.run_angle(90, 90)
sensor_motor.run_angle(90, -90) 
```

#### The test program used to test the color sensor's color sensing ability.
```python
"""Tests the colour sensor, to detect the two good blocks (red or yellow), making one beep
unrecognised blocks or undetect makes two beeps."""


if colour_sensor.color() == Color.RED or Color.YELLOW:
    #pick up here
    speaker.beep()
else:
    #move back here and turn 90 degrees
    speaker.beep()
    speaker.beep()
```

## **Testing and Debugging**
| Test Case | Input     | Expected Output   |
|---------- |---------- |----------------   |
|red/yellow block|Colour sensor finds a red/yellow block|The robot will use a mechanism to take the block to the start|
#### The main features of the code are to detect the colour and do an action depending on the colour of the block, if the colour of the block is red or yellow it will pick it up and take it to the start. The code could be improved by putting functions in to make it more efficient or to make it faster. Our test was succesful in doing what it was meant to do and it gave us a good idea on how to use the colour sensor.
```python
if colour_sensor.color() == Color.RED or Color.YELLOW:
    #pick up block
    speaker.beep()
else:
    #go around it
    speaker.beep()
    speaker.beep()
```

| Test Case | Input     | Expected Output   |
|---------- |---------- |----------------   |
|non red/yellow block|Colour sensor finds a non red/yellow block|The robot will move back by 5cm, turn left by 90 degrees, and move forward by 5cm|
#### The main features of the code are to detect the colour and do an action depending on the colour of the block, if the colour of the block is not red or yellow it will avoid the block. The code could be improved by putting functions in to make it more efficient or to make it faster. Our test was succesful in doing what it was meant to do and it gave us a good idea on how to use the colour sensor.
```python
if colour_sensor.color() == Color.RED or Color.YELLOW:
    #pick up block
    speaker.beep()
else:
    #go around it
    speaker.beep()
    speaker.beep()
```

| Test Case | Input     | Expected Output   |
|---------- |---------- |----------------   |
|block found|The ultrasonic sensor finds a block near infront of the robot|The robot will move forward until the ultrasonic sensor detects that the block is within 1cm|
#### The main features of the code are to move forward until and object is within a set distance. The code could be improved by making it move in smaller movements so that it is more accurate. The test was successfull, the only thing that challenged us was getting the variables right, like the detect distance and how far the robot moved to be accurate.
```python
while ultrasonic_sensor.distance() > detect_distance:
    #move forward if block not within detect distnace
    robot.straight(10)
#beep when within distance
speaker.beep()
```

| Test Case | Input     | Expected Output   |
|---------- |---------- |----------------   |
|avoiding leaving the designated area|The colour sensor detects the colour black|The robot will move rotate until it no longer detects black|
#### The main features of the code are to use the colour sensor to ensure the robot stays within the area. The code could be improved by giving an output on the screen about the variables. The test was succesful and the robot stayed on the challenge mat.
```python
while True:
    deviation = line_sensor.reflection() - threshold

    turn_rate = PROPORTIONAL_GAIN * deviation #sets the turn rate dynamically

    robot.drive(DRIVE_SPEED, turn_rate) #combines the drive speed and the turn rate

    wait(10)
```

## **Peer Evaluation**
### **Fraser**

#### When rating 1-5 with 1 being lacklustre effort and 5 being outstanding effort, how much effort do you feel this group member put into this project?

#### 3/5

#### Fraser put in a decent amount of work and made a peice of code that we later incorperated bits into the final peice of code, he also helped in coming up with solutions to problems we had.
---
#### When rating 1-5 with 1 being not at all and 5 being an exceptional amount, how much did this team member contribute to the team's efforts throughout this project?

#### 3/5

#### Fraser helped with lots of stuff and contributed a good amount into the team project, helping with problems and helping to build the robot.
---
#### When rating 1-5 with 1 being entirely non-functional and 5 being completely functional, how effective was this team member's final test case?

#### 3/5

#### His code had a few errors and the robot didnt run how it was supposed to, but his code made sense and was logical even though the robot wasnt doing anything it was supposed to do.
---
#### When rating 1-5 with 1 being not well at all and 5 being exceptionally well, how well do you think this team member performed throughout all stages of the project?

#### 4/5

#### Fraser performed well throughout all stages of the project helping to create the final peice of code we have now.
---
### **Charles**

#### When rating 1-5 with 1 being lacklustre effort and 5 being outstanding effort, how much effort do you feel this group member put into this project?

#### 5/5

#### Charles put in a lot of effor and work into this project and peiced together all of our code into one big chunk. He was the one who finalised everything to make our code as best as it could be.
---
#### When rating 1-5 with 1 being not at all and 5 being an exceptional amount, how much did this team member contribute to the team's efforts throughout this project?

#### 5/5

#### Charles contributed alot in the team project mostly on the coding aspect of the project creating many tests that would later be used in the final version of the code.
---
#### When rating 1-5 with 1 being entirely non-functional and 5 being completely functional, how effective was this team member's final test case?

#### 5/5

#### Most, if not all of his code worked, and even if it didnt he would find the solution to it. His code was very effective and he made everything work in the end.
---
#### When rating 1-5 with 1 being not well at all and 5 being exceptionally well, how well do you think this team member performed throughout all stages of the project?

#### 5/5

#### Charles performed very well throughout the whole project managing everything and making everything work. His contributions were very important to the project and without his effort we would have got as far as we did.

## **Final Evaluation**
#### My final test in relation to the functional criteria wasnt great, the robot didnt work how it was meant to mainly because the sensor wasnt in line with the block causing it to run into the block and keep moving forward. The robot couldnt move the block, but it could detect and classify the blocks colour, it just wasnt able to do that in the final test because that part of the code was after where it failed.
---
#### My final test in relation to the non-functional criteria also wasnt great due to the fact that it wasnt efficient and it didnt move fast because it had to be accurate without making and mistakes. We could have made the robot move faster but it would have increased the amount of potential errors.
---
#### My groups final performance in relation to the identified need was mildly underwhelming, but if we had a bit more time we could have achieved the goal and made a finished working robot that could work properly.
---
#### Our teams time management wasnt too great as in the end we did not entirely achive a final working robot. This was mainly because we spent alot of time on the theory side if the task in class, when we should have been working on testing the robot.
---
#### Our team collaborated well and we communicated to eachother alot to attempt trying to solve the problems we had with our robot. We communicated alot on how to fix our code, and I think the communication helped alot in the task.
---
#### We could have improved on many things in this project to complete it faster and better. We could have heavily improved on our time management and worked on the project efficiently. Another thing we could have improved on is splitting the task up, as in one person could work on one thing like picking up the block or detecting the block, but instead we all tried to work on one thing at a time.