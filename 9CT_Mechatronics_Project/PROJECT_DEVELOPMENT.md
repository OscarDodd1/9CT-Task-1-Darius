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
    - Inputs: The colour sensor
    - Action: 
    - Expected Outcome: 
3. Block avoidance
    - Scenario: 
    - Inputs: 
    - Action: 
    - Expected Outcome: 
4. Block movement
    - Scenario: 
    - Inputs: 
    - Action: 
    - Expected Outcome: 

### Test cases

### Non-functional requirements

## Design

## Development and Integration

## Testing and Debugging

## Evaluation