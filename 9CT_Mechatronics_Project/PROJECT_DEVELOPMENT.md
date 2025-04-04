# 9CT Assessment Task 1
### By Oscar Dodd

## Requirements outline
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

## Design
### Algoriths
1. Algorithm 1
2. Algorithm 2
3. Algorithm 3

## Development and Integration

## Testing and Debugging

## Evaluation