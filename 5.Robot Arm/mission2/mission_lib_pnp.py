import math
from time import sleep

class Movement:
    """
    Functions for robot arm movements
    
    :Arm: Robot Arm object
    :release_angle: Angle when the gripper is opened
    :grap_angle: Angle when the gripper is closed
    :initial_release_position: Initial position with gripper is opened
    :initial_grap_position: Initial position with gripper is closed
    :time: The time length for the movement
    """

    def __init__(self, Arm):
        self.Arm = Arm
        self.release_angle = 30
        self.grap_angle = 170
        
        self.initial_release_position = [90, 90, 0, 90, 90, self.release_angle]
        self.initial_grap_position = [90, 90, 0, 90, 90, self.grap_angle]

    def move_to_initial_position(self, time) :
        """
        Move the Robot Arm to its initial position. 
        
        :param time: Movement time for the Robot Arm 
        :type: int
        
        """

        self.Arm.Arm_serial_servo_write6_array(self.initial_release_position, time)
        sleep(2)
        
    def move_to_positions(self, angle, time):
        """
        Rotates the robot arm by an angle. Designate 4 positions to pick and place and add them to the list.
        
        :param time: Movement time for the Robot Arm
        :param angle: Rotation angle for the Robot Arm 
        :type: int
        
        """

        self.move_release_position = [angle, 90, 0, 90, 90, self.release_angle]
        self.move_grap_position = [angle, 90, 0, 90, 90, self.grap_angle]
        self.lower_release_position = [angle, 0, 45, 45, 90, self.release_angle]
        self.lower_grap_position = [angle, 0, 45, 45, 90, self.grap_angle]
        
        positions = [
            self.initial_release_position, self.move_release_position, self.lower_release_position, 
            self.lower_grap_position, self.move_grap_position, self.initial_grap_position
        ]
        """
        The robot arm sequentially moves through the positions in the list.
        
        """
            
        for position in positions:
            self.Arm.Arm_serial_servo_write6_array(position, time)
            sleep(2)